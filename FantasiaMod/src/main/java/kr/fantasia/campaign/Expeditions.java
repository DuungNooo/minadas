package kr.fantasia.campaign;

import net.minecraft.server.level.ServerPlayer;
import net.minecraft.server.level.ServerLevel;
import net.minecraft.world.entity.*;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.entity.npc.Villager;
import net.minecraft.world.item.*;
import net.minecraft.network.chat.Component;
import net.minecraft.core.particles.ParticleTypes;
import net.minecraft.world.phys.Vec3;
import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

/** Persistent authored objectives; active encounters are disposable and restarted after disconnect. */
public final class Expeditions {
    public record Step(String title,String text,String kind,int x,int z,List<Integer> sequence) {}
    public record Chapter(String id,String title,String npc,int stage,List<Step> steps) {}
    public record Catalog(List<Chapter> chapters) {}
    public static final Catalog CATALOG=load();
    private static final class Encounter {
        final String chapter;final int step;final List<UUID> mobs=new ArrayList<>();
        UUID escort;UUID boss;long age;Vec3 warning;net.minecraft.server.level.ServerBossEvent bossBar;
        Encounter(String chapter,int step){this.chapter=chapter;this.step=step;}
    }
    private static final Map<UUID,Encounter> ACTIVE=new HashMap<>();
    private static Catalog load(){try(var in=Objects.requireNonNull(Expeditions.class.getResourceAsStream("/fantasia/expeditions.json"));var reader=new InputStreamReader(in,StandardCharsets.UTF_8)){return Content.GSON.fromJson(reader,Catalog.class);}catch(IOException e){throw new UncheckedIOException(e);}}
    public static Chapter chapter(String id){return CATALOG.chapters().stream().filter(c->c.id().equals(id)).findFirst().orElse(null);}
    public static int progress(ServerPlayer p,Chapter c){return Progress.data(p).getInt("exp_"+c.id());}
    public static boolean done(ServerPlayer p,String id){var c=chapter(id);return c!=null&&progress(p,c)>=c.steps().size();}
    public static void addOptions(ServerPlayer p,Entity npc,String id,List<Menus.Option> options){
        for(var c:CATALOG.chapters())if(c.npc().equals(id)&&Progress.score(p,"fa_stage")>=c.stage()){
            options.add(new Menus.Option((done(p,c.id())?"완료 · ":"원정 · ")+c.title(),()->brief(p,npc,c)));
        }
    }
    private static void brief(ServerPlayer p,Entity npc,Chapter c){
        int step=progress(p,c);String body="원정 기록 "+Math.min(step,c.steps().size())+" / "+c.steps().size()+"\n\n";
        if(step>=c.steps().size())body+=c.steps().getLast().text();
        else body+="다음 목표: "+c.steps().get(step).title()+"\n기록 조사, 실전, 공명 장치, 호위와 지휘관전을 통해 진실을 찾습니다.\n\n실패해도 완료한 목표는 보존됩니다. 호위 대상이 쓰러지거나 지역을 이탈하면 현재 전투만 다시 시작합니다.";
        var opts=new ArrayList<Menus.Option>();
        if(step<c.steps().size())opts.add(new Menus.Option("원정 출발 / 체크포인트 복귀",()->travel(p,c)));
        opts.add(new Menus.Option("돌아가기",()->Menus.npc(p,npc)));
        Menus.show(p,c.title(),body,npc,opts);
    }
    private static void travel(ServerPlayer p,Chapter c){
        if(c.id().equals("blackout")&&Progress.score(p,"fa_gear")==0){message(p,"먼저 카일에게 훈련 장비를 받아 착용해 주세요.");return;}
        if(Progress.score(p,"fa_stage")<c.stage()||!Progress.has(p,"exam/complete")){message(p,"입학 검사를 완료하고 이야기 진행 조건을 확인하세요.");return;}
        var obj=p.getScoreboard().getObjective("fa_world");
        var score=obj==null?null:p.getScoreboard().getPlayerScoreInfo(net.minecraft.world.scores.ScoreHolder.forNameOnly("#exp_ready"),obj);
        if(score==null||score.value()!=1){message(p,"원정 지역을 생성하고 있습니다. 잠시 후 다시 대화해 주세요.");return;}
        if(c.id().equals("cult_hideout")&&!done(p,"buried_lab")){message(p,"노아의 지하 연구소 원정에서 교수의 단서를 먼저 찾아주세요.");return;}
        abort(p);var s=c.steps().get(Math.clamp(progress(p,c),0,c.steps().size()-1));
        Progress.command(p,"execute in fantasia:campaign run tp @s "+s.x()+" 65 "+(s.z()+9));
        message(p,"공중에 표시된 목표를 우클릭하세요. J 키의 기록에서 아카데미로 돌아갈 수 있습니다.");
    }
    public static boolean station(Entity e){return e.getTags().contains("fa_exp_station");}
    public static void interact(ServerPlayer p,Entity e){
        if(!FantasiaMod.inCampaign(p)||p.distanceToSqr(e)>36)return;
        for(var c:CATALOG.chapters())for(int i=0;i<c.steps().size();i++)if(e.getTags().contains("fa_exp_"+c.id()+"_"+i)){
            final int step=i;
            if(progress(p,c)!=i||Progress.score(p,"fa_stage")<c.stage()){message(p,"현재 원정 순서와 맞지 않는 기록입니다. 안내 NPC에게 진행을 확인하세요.");return;}
            var s=c.steps().get(i);
            var opts=new ArrayList<Menus.Option>();String body=s.text();
            switch(s.kind()){
                case "investigate","evidence"->opts.add(new Menus.Option("기록 확보",()->advance(p,c,step)));
                case "sequence"->{
                    body+="\n\n공명 규칙: "+s.sequence().stream().map(v->List.of("청색","황색","적색").get(v)).reduce((a,b)->a+" → "+b).orElse("")+"\n장치가 잘못 반응하면 처음부터 다시 조정합니다.";
                    for(int j=0;j<3;j++){int rune=j;opts.add(new Menus.Option(List.of("청색 공명기","황색 공명기","적색 공명기").get(j),()->sequence(p,e,c,step,rune)));}
                }
                default->opts.add(new Menus.Option(ACTIVE.containsKey(p.getUUID())?"전투 진행 중":"작전 시작",()->start(p,c,step)));
            }
            Menus.show(p,s.title(),body,e,opts);return;
        }
    }
    private static void sequence(ServerPlayer p,Entity station,Chapter c,int step,int rune){
        if(progress(p,c)!=step)return;var d=Progress.data(p);String key="exp_rune_"+c.id();int count=Math.clamp(d.getInt(key),0,2);
        if(c.steps().get(step).sequence().get(count)!=rune){d.putInt(key,0);message(p,"공명이 흐트러졌습니다. 첫 장치부터 다시 맞춰주세요.");}
        else if(count==2){d.remove(key);advance(p,c,step);return;}
        else {d.putInt(key,count+1);message(p,"공명 "+(count+1)+" / 3");}
        interact(p,station);
    }
    private static void start(ServerPlayer p,Chapter c,int step){
        if(ACTIVE.containsKey(p.getUUID())||progress(p,c)!=step)return;
        var s=c.steps().get(step);var encounter=new Encounter(c.id(),step);ACTIVE.put(p.getUUID(),encounter);
        boolean boss=s.kind().equals("boss");int count=boss?3:5;
        for(int i=0;i<count;i++){
            EntityType<? extends Mob> type=(i%2==0?EntityType.HUSK:EntityType.STRAY);
            Mob mob=type.create(p.serverLevel());if(mob==null)continue;
            mob.moveTo(s.x()-8+i*4,65,s.z()-6,0,0);mob.setPersistenceRequired();mob.setTarget(p);
            mob.addTag("fa_exp_enemy");mob.getPersistentData().putUUID("fa_owner",p.getUUID());
            if(boss&&i==0){mob.getAttribute(Attributes.MAX_HEALTH).setBaseValue(80+c.stage()*12);mob.setHealth(mob.getMaxHealth());mob.setCustomName(Component.literal(s.title()));mob.setCustomNameVisible(true);
                encounter.boss=mob.getUUID();
                encounter.bossBar=new net.minecraft.server.level.ServerBossEvent(Component.literal(s.title()),net.minecraft.world.BossEvent.BossBarColor.PURPLE,net.minecraft.world.BossEvent.BossBarOverlay.PROGRESS);
                encounter.bossBar.addPlayer(p);
            }
            if(type==EntityType.STRAY)mob.setItemSlot(EquipmentSlot.MAINHAND,new ItemStack(Items.BOW));
            mob.setDropChance(EquipmentSlot.MAINHAND,0);p.serverLevel().addFreshEntity(mob);encounter.mobs.add(mob.getUUID());
        }
        if(s.kind().equals("escort")){
            Villager villager=EntityType.VILLAGER.create(p.serverLevel());
            if(villager!=null){villager.moveTo(s.x(),65,s.z()-8,0,0);villager.setCustomName(Component.literal("구조 대상 · 함께 이동하세요"));villager.setCustomNameVisible(true);villager.setPersistenceRequired();villager.addTag("fa_exp_escort");p.serverLevel().addFreshEntity(villager);encounter.escort=villager.getUUID();}
            message(p,"구조 대상은 가까이 있으면 따라옵니다. 적을 제압하고 방의 남동쪽 밝은 기둥까지 안내하세요.");
        }else message(p,boss?"경고 입자가 생기면 그 자리에서 벗어나세요!":"통로의 적을 제압하세요. 이탈하면 작전만 다시 시작합니다.");
    }
    public static void tick(ServerPlayer p){
        var e=ACTIVE.get(p.getUUID());if(e==null)return;var c=chapter(e.chapter);var s=c.steps().get(e.step);
        if(!p.isAlive()||!FantasiaMod.inCampaign(p)||p.position().distanceToSqr(new Vec3(s.x(),65,s.z()))>2500||++e.age>12000){abort(p);message(p,"현재 작전이 중단되었습니다. 완료 기록은 유지됩니다.");return;}
        e.mobs.removeIf(id->{var mob=p.serverLevel().getEntity(id);return mob==null||!mob.isAlive();});
        if(e.bossBar!=null){
            var entity=p.serverLevel().getEntity(e.boss);
            if(entity instanceof net.minecraft.world.entity.LivingEntity living&&living.isAlive())e.bossBar.setProgress(living.getHealth()/living.getMaxHealth());
            else e.bossBar.setProgress(0);
        }
        if(s.kind().equals("boss")&&!e.mobs.isEmpty()){
            if(e.age%100==1){e.warning=p.position();message(p,"마력이 모입니다. 표시된 자리에서 이동하세요!");}
            if(e.warning!=null&&e.age%100<=30)p.serverLevel().sendParticles(ParticleTypes.FLAME,e.warning.x,65.2,e.warning.z,8,2,.1,2,.01);
            if(e.warning!=null&&e.age%100==31){if(p.position().distanceToSqr(e.warning)<16)p.hurt(p.damageSources().magic(),6);e.warning=null;}
        }
        boolean escortReady=true;
        if(e.escort!=null){
            var entity=p.serverLevel().getEntity(e.escort);
            if(!(entity instanceof Villager villager)||!villager.isAlive()){abort(p);message(p,"구조 대상이 쓰러졌습니다. 목표를 다시 시작할 수 있습니다.");return;}
            escortReady=villager.position().distanceToSqr(new Vec3(s.x()+10,65,s.z()+10))<16;
            if(e.age%20==0){
                if(villager.distanceToSqr(p)<100&&!escortReady)villager.getNavigation().moveTo(p,0.75);
                for(var id:e.mobs){var enemy=p.serverLevel().getEntity(id);if(enemy instanceof Mob m)m.setTarget(villager);}
            }
        }
        if(e.mobs.isEmpty()&&escortReady){abort(p);advance(p,c,e.step);}
    }
    public static void abort(ServerPlayer p){
        var e=ACTIVE.remove(p.getUUID());if(e==null)return;
        if(e.bossBar!=null)e.bossBar.removeAllPlayers();
        for(ServerLevel level:p.server.getAllLevels()){
            for(var id:e.mobs){var entity=level.getEntity(id);if(entity!=null)entity.discard();}
            if(e.escort!=null){var entity=level.getEntity(e.escort);if(entity!=null)entity.discard();}
        }
    }
    public static void clear(){ACTIVE.clear();}
    private static void advance(ServerPlayer p,Chapter c,int expected){
        if(progress(p,c)!=expected)return;
        Progress.data(p).putInt("exp_"+c.id(),expected+1);
        if(expected+1==c.steps().size()){
            p.giveExperiencePoints(60+c.stage()*20);
            var stack=new ItemStack(Items.AMETHYST_SHARD,3);if(!p.getInventory().add(stack))p.drop(stack,false);
            var npc=Content.NPCS.get(c.npc());if(npc!=null&&npc.relation()){
                String key="fantasia_affection_"+c.npc();Progress.data(p).putInt(key,Math.min(100,Progress.data(p).getInt(key)+15));
                if(Progress.data(p).getInt(key)>=80)Progress.grant(p,"bond/"+c.npc());
            }
            message(p,"원정 완료: "+c.title()+". NPC에게 돌아가 이야기를 이어가세요.");
        }else{
            var next=c.steps().get(expected+1);message(p,"기록 저장. 다음 목표: "+next.title()+" (X "+next.x()+", Z "+next.z()+")");
        }
    }
    public static String required(int action){return switch(action){case 101,102,103,104->"blackout";case 20->"mine_depths";case 21->"canal_rescue";case 22->"forest_heart";case 23->"storm_signal";case 30->"capital_refuge";case 31->"cult_hideout";case 40->"north_watch";case 41->"east_garden";case 42->"south_forge";case 50->"castle_memory";default->null;};}
    public static void journal(ServerPlayer p,List<Menus.Option> opts){
        opts.add(new Menus.Option("원정 기록",()->{
            StringBuilder body=new StringBuilder();for(var c:CATALOG.chapters())body.append(c.title()).append(" · ").append(progress(p,c)).append(" / ").append(c.steps().size()).append("\n");
            Menus.show(p,"원정 기록",body.toString(),null,List.of(new Menus.Option("돌아가기",()->Menus.journal(p))));
        }));
        if(FantasiaMod.inCampaign(p)&&p.getX()>900)opts.add(new Menus.Option("원정 중단 · 아카데미로",()->{abort(p);Progress.command(p,"execute in fantasia:campaign run tp @s 0 65 -8");}));
    }
    private static void message(ServerPlayer p,String message){p.sendSystemMessage(Component.literal(message));}
    private Expeditions(){}
}
