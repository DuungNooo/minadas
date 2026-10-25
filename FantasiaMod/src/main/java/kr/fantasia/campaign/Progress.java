package kr.fantasia.campaign;

import net.minecraft.nbt.*;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.storage.LevelResource;
import java.nio.file.*;

public final class Progress {
    public static CompoundTag data(Player p){
        var root=p.getPersistentData();
        if(!root.contains(Player.PERSISTED_NBT_TAG,Tag.TAG_COMPOUND))root.put(Player.PERSISTED_NBT_TAG,new CompoundTag());
        var persisted=root.getCompound(Player.PERSISTED_NBT_TAG);
        if(!persisted.contains("Fantasia",Tag.TAG_COMPOUND))persisted.put("Fantasia",new CompoundTag());
        return persisted.getCompound("Fantasia");
    }
    public static void migrate(ServerPlayer player){
        var dest=data(player);
        if(dest.getBoolean("migrated"))return;
        // Read old KubeJS data even if KubeJS itself has been removed.
        Path file=player.server.getWorldPath(LevelResource.PLAYER_DATA_DIR).resolve(player.getUUID()+".dat");
        try {
            CompoundTag full=Files.isRegularFile(file)?NbtIo.readCompressed(file,NbtAccounter.unlimitedHeap()):new CompoundTag();
            var old=full.getCompound("KubeJSPersistentData");
            for(String key:old.getAllKeys())if(key.startsWith("fantasia_"))dest.put(key,old.get(key).copy());
            dest.putBoolean("migrated",true);
        } catch(Exception e){FantasiaMod.LOGGER.error("Could not migrate Fantasia progress for {}",player.getUUID(),e);}
    }
    public static void copy(Player from,Player to){
        var old=from.getPersistentData().getCompound(Player.PERSISTED_NBT_TAG);
        to.getPersistentData().put(Player.PERSISTED_NBT_TAG,old.copy());
    }
    public static boolean has(ServerPlayer p,String path){
        var a=p.server.getAdvancements().get(ResourceLocation.parse("fantasia_research:"+path));
        return a!=null&&p.getAdvancements().getOrStartProgress(a).isDone();
    }
    public static void grant(ServerPlayer p,String path){
        var a=p.server.getAdvancements().get(ResourceLocation.parse("fantasia_research:"+path));
        if(a!=null)for(var c:a.value().criteria().keySet())p.getAdvancements().award(a,c);
    }
    public static void revoke(ServerPlayer p,String path){
        var a=p.server.getAdvancements().get(ResourceLocation.parse("fantasia_research:"+path));
        if(a!=null)for(var c:a.value().criteria().keySet())p.getAdvancements().revoke(a,c);
    }
    public static int score(ServerPlayer p,String objective){
        var board=p.getScoreboard();var obj=board.getObjective(objective);
        if(obj==null)return 0;var value=board.getPlayerScoreInfo(p,obj);return value==null?0:value.value();
    }
    public static void command(ServerPlayer p,String command){
        p.server.getCommands().performPrefixedCommand(p.createCommandSourceStack().withPermission(2).withSuppressedOutput(),command);
    }
    private Progress(){}
}
