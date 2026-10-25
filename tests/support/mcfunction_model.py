"""Small, deliberately bounded executor for campaign logic regression tests.

This is not Minecraft or an assertion that datapacks load in Minecraft. It
executes the shipped function bodies and fails on unsupported logic commands;
presentation/world-rendering commands are explicitly recorded but not rendered.
"""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from pathlib import Path
import json
import math
import re


def words(text: str) -> list[str]:
    result, start, depth, quote, escaped = [], 0, 0, None, False
    for i, char in enumerate(text):
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
        elif char in "\"'":
            quote = char
        elif char in "[{(":
            depth += 1
        elif char in "]})":
            depth -= 1
        elif char.isspace() and depth == 0:
            if i > start:
                result.append(text[start:i])
            start = i + 1
    if start < len(text):
        result.append(text[start:])
    return result


def fields(text: str) -> list[str]:
    result, start, depth, quote, escaped = [], 0, 0, None, False
    for i, char in enumerate(text):
        if quote:
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == quote:
                quote = None
        elif char in "\"'":
            quote = char
        elif char in "[{(":
            depth += 1
        elif char in "]})":
            depth -= 1
        elif char == "," and depth == 0:
            result.append(text[start:i].strip())
            start = i + 1
    result.append(text[start:].strip())
    return result


def in_range(value: float | None, spec: str) -> bool:
    if value is None:
        return False
    if ".." not in spec:
        return value == float(spec)
    low, high = spec.split("..", 1)
    return (not low or value >= float(low)) and (not high or value <= float(high))


@dataclass
class Entity:
    name: str
    kind: str = "minecraft:player"
    pos: tuple[float, float, float] = (0, 65, 0)
    dimension: str = "fantasia:campaign"
    tags: set[str] = field(default_factory=set)
    scores: dict[str, int] = field(default_factory=dict)
    advancements: set[str] = field(default_factory=set)
    inventory: dict[str, int] = field(default_factory=dict)
    nbt: dict = field(default_factory=dict)
    gamemode: str = "adventure"
    online: bool = True
    alive: bool = True


@dataclass
class Context:
    source: Entity | None = None
    pos: tuple[float, float, float] = (0, 0, 0)
    dimension: str = "minecraft:overworld"


class FunctionReturn(Exception):
    def __init__(self, value: int):
        self.value = value


class World:
    def __init__(self, root: Path):
        self.root = root
        self.entities: list[Entity] = []
        self.fake_scores: dict[tuple[str, str], int] = {}
        self.objectives: set[str] = set()
        self.messages: list[tuple[str, str]] = []
        self.effects: list[tuple[str, ...]] = []
        self.calls: list[str] = []
        self.ignored: list[str] = []
        self.scheduled: dict[str, int] = {}
        self.gametime = 0
        self.commands = 0
        self.blocks: dict[tuple[str, tuple[int, int, int]], str] = {}

    def player(self, name="Tester", pos=(0, 65, 0), dimension="fantasia:campaign"):
        e = Entity(name=name, pos=pos, dimension=dimension)
        self.entities.append(e)
        return e

    def context(self, entity=None):
        return Context(entity, entity.pos, entity.dimension) if entity else Context()

    def selected(self, selector: str, context: Context) -> list[Entity]:
        if not selector.startswith("@"):
            return [e for e in self.entities if e.name == selector and e.online and e.alive]
        kind = selector[:2]
        options = []
        if "[" in selector:
            options = [v.split("=", 1) for v in fields(selector[selector.index("[") + 1:-1])]
        if kind == "@s":
            candidates = [context.source] if context.source and context.source.online and context.source.alive else []
        elif kind in ("@a", "@p", "@r"):
            candidates = [e for e in self.entities if e.kind == "minecraft:player" and e.online and e.alive]
        elif kind == "@e":
            candidates = [e for e in self.entities if e.online and e.alive and e.dimension == context.dimension]
        else:
            raise NotImplementedError(selector)
        origin = list(context.pos)
        for key, val in options:
            if key in ("x", "y", "z"):
                origin["xyz".index(key)] = float(val)
        for key, val in options:
            if key == "tag":
                candidates = [e for e in candidates if (val[1:] not in e.tags if val.startswith("!") else val in e.tags)]
            elif key == "type":
                excluded = val.startswith("!")
                target = val.lstrip("!")
                if ":" not in target:
                    target = "minecraft:" + target
                candidates = [e for e in candidates if (e.kind != target if excluded else e.kind == target)]
            elif key == "scores":
                for item in fields(val[1:-1]):
                    objective, spec = item.split("=", 1)
                    candidates = [e for e in candidates if in_range(e.scores.get(objective), spec)]
            elif key == "advancements":
                for item in fields(val[1:-1]):
                    advancement, state = item.split("=", 1)
                    if state not in ("true", "false"):
                        raise NotImplementedError("criterion-specific advancement selector")
                    candidates = [e for e in candidates if (advancement in e.advancements) == (state == "true")]
            elif key == "distance":
                candidates = [e for e in candidates if e.dimension == context.dimension and in_range(math.dist(e.pos, origin), val)]
            elif key in ("dx", "dy", "dz"):
                axis = "xyz".index(key[-1])
                lo, hi = sorted((origin[axis], origin[axis] + float(val)))
                candidates = [e for e in candidates if e.dimension == context.dimension and lo <= e.pos[axis] < hi + 1]
            elif key == "gamemode":
                candidates = [e for e in candidates if (e.gamemode != val[1:] if val.startswith("!") else e.gamemode == val)]
            elif key == "name":
                candidates = [e for e in candidates if (e.name != val[1:] if val.startswith("!") else e.name == val)]
            elif key == "nbt":
                raise NotImplementedError("NBT selector: " + selector)
            elif key not in ("x", "y", "z", "limit", "sort"):
                raise NotImplementedError("Selector option: " + key)
        opts = dict(options)
        if opts.get("sort") == "nearest" or kind == "@p":
            candidates.sort(key=lambda e: math.dist(e.pos, origin))
        limit = int(opts.get("limit", 1 if kind in ("@p", "@r") else len(candidates)))
        return candidates[:limit]

    def holders(self, selector, context):
        return self.selected(selector, context) if selector.startswith("@") else [next((e for e in self.entities if e.name == selector), selector)]

    def score(self, holder: str | Entity, objective: str):
        return holder.scores.get(objective) if isinstance(holder, Entity) else self.fake_scores.get((holder, objective))

    def setscore(self, holder: str | Entity, objective: str, value: int):
        if isinstance(holder, Entity):
            holder.scores[objective] = int(value)
        else:
            self.fake_scores[(holder, objective)] = int(value)

    def position(self, parts, context):
        out = []
        for axis, val in enumerate(parts):
            if val.startswith("^"):
                raise NotImplementedError("local coordinates")
            out.append(context.pos[axis] + float(val[1:] or 0) if val.startswith("~") else float(val))
        return tuple(out)

    def function(self, identifier: str, player=None, context=None):
        context = context or self.context(player)
        namespace, path = identifier.split(":", 1)
        files = list(self.root.glob(f"*/data/{namespace}/function/{path}.mcfunction"))
        if not files:
            raise FileNotFoundError(identifier)
        if len(files) != 1:
            raise AssertionError("Conflicting function: " + identifier)
        self.calls.append(identifier)
        result = 0
        try:
            for line in files[0].read_text().splitlines():
                line = line.strip()
                if line and not line.startswith("#"):
                    result = self.command(line, context)
        except FunctionReturn as ret:
            return ret.value
        return result

    def execute(self, w, context):
        if not w:
            return 1
        op, rest = w[0], w[1:]
        if op == "run":
            return self.command(" ".join(rest), context)
        if op == "as":
            return sum(self.execute(rest[1:], replace(context, source=e)) for e in self.selected(rest[0], context))
        if op == "at":
            return sum(self.execute(rest[1:], replace(context, pos=e.pos, dimension=e.dimension)) for e in self.selected(rest[0], context))
        if op == "in":
            return self.execute(rest[1:], replace(context, dimension=rest[0]))
        if op == "positioned":
            if rest[0] == "as":
                return sum(self.execute(rest[2:], replace(context, pos=e.pos)) for e in self.selected(rest[1], context))
            return self.execute(rest[3:], replace(context, pos=self.position(rest[:3], context)))
        if op in ("if", "unless"):
            kind = rest[0]
            if kind == "entity":
                passed, offset = bool(self.selected(rest[1], context)), 2
            elif kind == "dimension":
                passed, offset = rest[1] == context.dimension, 2
            elif kind == "score":
                targets = self.holders(rest[1], context)
                value = self.score(targets[0], rest[2]) if len(targets) == 1 else None
                if rest[3] == "matches":
                    passed, offset = in_range(value, rest[4]), 5
                else:
                    other = self.holders(rest[4], context)
                    rhs = self.score(other[0], rest[5]) if len(other) == 1 else None
                    if value is None or rhs is None:
                        passed = False
                    else:
                        passed = {"=": value == rhs, "<": value < rhs, ">": value > rhs, "<=": value <= rhs, ">=": value >= rhs}[rest[3]]
                    offset = 6
            elif kind == "block":
                pos = tuple(int(v) for v in self.position(rest[1:4], context))
                passed, offset = self.blocks.get((context.dimension, pos), "minecraft:air") == rest[4], 5
            elif kind == "data" and rest[1] == "entity":
                entities = self.selected(rest[2], context)
                passed, offset = bool(entities and rest[3] in entities[0].nbt), 4
            else:
                raise NotImplementedError("execute condition: " + " ".join(rest))
            return self.execute(rest[offset:], context) if passed == (op == "if") else 0
        if op == "store" and rest[1] == "score":
            result = self.execute(rest[4:], context)
            value = result if rest[0] == "result" else int(result != 0)
            for holder in self.holders(rest[2], context):
                self.setscore(holder, rest[3], value)
            return result
        raise NotImplementedError("execute: " + " ".join(w))

    def command(self, command: str, context: Context):
        self.commands += 1
        if self.commands > 1_000_000:
            raise RuntimeError("Command cycle/limit")
        w = words(command)
        op = w[0]
        if op == "execute":
            return self.execute(w[1:], context)
        if op == "function":
            return self.function(w[1], context=context)
        if op == "return":
            raise FunctionReturn(self.command(" ".join(w[2:]), context) if w[1] == "run" else (0 if w[1] == "fail" else int(w[1])))
        if op == "scoreboard":
            if w[1] == "objectives":
                if w[2] == "add":
                    self.objectives.add(w[3])
                return 1
            action, holder, objective = w[2:5]
            targets = self.holders(holder, context)
            if action == "enable":
                return len(targets)
            for target in targets:
                previous = self.score(target, objective)
                if action == "get":
                    return previous or 0
                if action == "reset":
                    if isinstance(target, Entity):
                        target.scores.pop(objective, None)
                    else:
                        self.fake_scores.pop((target, objective), None)
                    continue
                if action in ("set", "add", "remove"):
                    value = int(w[5]) if action == "set" else (previous or 0) + int(w[5]) * (1 if action == "add" else -1)
                elif action == "operation":
                    source = self.holders(w[6], context)
                    if len(source) != 1:
                        raise NotImplementedError(command)
                    right = self.score(source[0], w[7])
                    if right is None:
                        continue
                    left = previous or 0
                    operators = {"=": lambda: right, "+=": lambda: left + right, "-=": lambda: left - right, "*=": lambda: left * right, "/=": lambda: left // right, "%=": lambda: left % right, "<": lambda: min(left, right), ">": lambda: max(left, right)}
                    value = operators[w[5]]()
                else:
                    raise NotImplementedError(command)
                self.setscore(target, objective, value)
            return len(targets)
        if op == "tag":
            targets = self.selected(w[1], context)
            for target in targets:
                getattr(target.tags, "add" if w[2] == "add" else "discard")(w[3])
            return len(targets)
        if op == "advancement":
            targets = self.selected(w[2], context)
            if w[3] != "only":
                raise NotImplementedError(command)
            for target in targets:
                getattr(target.advancements, "add" if w[1] == "grant" else "discard")(w[4])
            return len(targets)
        if op in ("tp", "teleport"):
            targets = self.selected(w[1], context)
            if len(w) < 5:
                raise NotImplementedError(command)
            pos = self.position(w[2:5], context)
            for target in targets:
                target.pos, target.dimension = pos, context.dimension
            return len(targets)
        if op == "summon":
            pos = self.position(w[2:5], context)
            nbt = " ".join(w[5:])
            match = re.search(r"Tags:\s*\[([^]]*)\]", nbt)
            tags = set(json.loads("[" + match[1] + "]")) if match else set()
            entity = Entity("mob_" + str(len(self.entities)), w[1], pos, context.dimension, tags=tags)
            health = re.search(r"Health:\s*([\d.]+)", nbt)
            entity.nbt["Health"] = float(health[1]) if health else 20
            self.entities.append(entity)
            return 1
        if op == "kill":
            targets = self.selected(w[1], context)
            for target in targets:
                target.alive = False
            return len(targets)
        if op == "give":
            item, amount = w[2].split("[", 1)[0], int(w[3]) if len(w) > 3 else 1
            targets = self.selected(w[1], context)
            for target in targets:
                target.inventory[item] = target.inventory.get(item, 0) + amount
            return len(targets)
        if op == "clear":
            targets = self.selected(w[1], context)
            count = 0
            for target in targets:
                item = w[2] if len(w) > 2 else None
                if item is None:
                    count += sum(target.inventory.values())
                    target.inventory.clear()
                else:
                    available = target.inventory.get(item, 0)
                    limit = int(w[3]) if len(w) > 3 else available
                    removed = available if limit == 0 else min(available, limit)
                    count += removed
                    if limit:
                        target.inventory[item] = available - removed
            return count
        if op == "gamemode":
            for target in self.selected(w[2], context):
                target.gamemode = w[1]
            return 1
        if op == "schedule":
            if w[1] == "clear":
                self.scheduled.pop(w[2], None)
            else:
                delay = int(w[3][:-1]) * (20 if w[3].endswith("s") else 1)
                self.scheduled[w[2]] = self.gametime + delay
            return 1
        if op == "data" and w[1:3] == ["get", "entity"]:
            targets = self.selected(w[3], context)
            return int(targets[0].nbt.get(w[4], 0) * (float(w[5]) if len(w) > 5 else 1)) if targets else 0
        if op == "setblock":
            pos = tuple(int(v) for v in self.position(w[1:4], context))
            self.blocks[(context.dimension, pos)] = w[4]
            return 1
        if op == "tellraw":
            self.messages.extend((e.name, w[2]) for e in self.selected(w[1], context))
            return 1
        if op in {"title", "particle", "playsound", "stopsound", "effect", "spawnpoint", "gamerule", "difficulty", "weather", "time", "bossbar", "attribute", "item", "fill", "forceload", "experience", "xp", "team"}:
            self.ignored.append(command)
            return 1
        raise NotImplementedError(command)
