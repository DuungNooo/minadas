These snapshots come from the `1.21.1-summary` tag of
https://github.com/misode/mcmeta, which publishes data extracted from Minecraft.

- `registries/data.json` → `minecraft_1.21.1_registries.json`
- `blocks/data.json` → `minecraft_1.21.1_blocks.json`
- `commands/data.json` → `minecraft_1.21.1_commands.json`

They pin compatibility checks to Minecraft 1.21.1 instead of a changing latest
release. The Mecha parser uses this exact command tree with its 1.21 parser
patches. Static parsing does not establish that a Minecraft server or a mod
combination has run successfully.
