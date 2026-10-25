package kr.fantasia.campaign;

import net.minecraft.server.level.ServerPlayer;
import java.util.*;

/** Local playtime evidence for pacing; never used as a content lock. */
public final class Playtime {
    private record Sample(net.minecraft.world.phys.Vec3 position,long lastActivity) {}
    private static final Map<UUID,Sample> SAMPLES=new HashMap<>();
    public static void activity(ServerPlayer p){SAMPLES.put(p.getUUID(),new Sample(p.position(),p.server.overworld().getGameTime()));}
    public static void tick(ServerPlayer p){
        if(p.tickCount%20!=0)return;
        if(!FantasiaMod.inCampaign(p)){SAMPLES.remove(p.getUUID());return;}
        var d=Progress.data(p);long now=p.server.overworld().getGameTime();var sample=SAMPLES.get(p.getUUID());
        if(sample==null||sample.position().distanceToSqr(p.position())>0.04){activity(p);sample=SAMPLES.get(p.getUUID());}
        d.putLong("campaign_play_ticks",d.getLong("campaign_play_ticks")+20);
        if(now-sample.lastActivity()<=1200)d.putLong("campaign_active_ticks",d.getLong("campaign_active_ticks")+20);
    }
    public static String display(ServerPlayer p){
        var d=Progress.data(p);return "캠페인 접속 "+format(d.getLong("campaign_play_ticks"))+" · 활동 추정 "+format(d.getLong("campaign_active_ticks"))+"\n활동은 이동·선택 후 1분 이내를 기준으로 기록합니다. 진행 조건에는 사용하지 않습니다.";
    }
    private static String format(long ticks){long minutes=ticks/1200;return minutes/60+"시간 "+minutes%60+"분";}
    public static void clear(ServerPlayer p){SAMPLES.remove(p.getUUID());}
    public static void clearAll(){SAMPLES.clear();}
    private Playtime(){}
}
