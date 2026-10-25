package kr.fantasia.campaign;

import com.google.gson.*;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public final class Content {
    public static final Gson GSON = new Gson();
    public record Choice(String text, Map<String,Integer> stat, Map<String,Integer> weapon, Map<String,Integer> affinity) {}
    public record Question(String title, String text, List<Choice> choices) {}
    public record Exam(List<Question> questions, LinkedHashMap<String,String> schools, LinkedHashMap<String,String> weapons) {}
    public record Action(String label, int id) {}
    public record NpcMenu(String title, String body, List<Action> actions) {}
    public record Npc(String name, String fav, boolean relation) {}
    public static final Exam EXAM = GSON.fromJson(read("exam"), Exam.class);
    public static final Map<String,NpcMenu> MENUS = map("menus", NpcMenu.class);
    public static final Map<String,Npc> NPCS = map("npcs", Npc.class);
    public static final Map<String,String> SPELLS = map("spells", String.class);
    public static final List<String> STATS = List.of("str","vit","agi","mag","mnd");
    private static JsonObject read(String name) {
        try(var stream=Objects.requireNonNull(Content.class.getResourceAsStream("/fantasia/"+name+".json"));
            var reader=new InputStreamReader(stream, StandardCharsets.UTF_8)) {
            return JsonParser.parseReader(reader).getAsJsonObject();
        } catch(IOException e) { throw new UncheckedIOException(e); }
    }
    private static <T> Map<String,T> map(String name, Class<T> type) {
        var out=new LinkedHashMap<String,T>();
        read(name).entrySet().forEach(e->out.put(e.getKey(),GSON.fromJson(e.getValue(),type)));
        return Collections.unmodifiableMap(out);
    }
    private Content() {}
}
