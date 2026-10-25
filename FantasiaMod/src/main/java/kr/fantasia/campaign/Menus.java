package kr.fantasia.campaign;

import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.Entity;
import net.minecraft.network.chat.Component;
import java.util.*;

public final class Menus {
    public record Option(String label,Runnable action) {}
    private record Session(String token, long expires, UUID npc, List<Option> options) {}
    private static final Map<UUID,Session> SESSIONS=new HashMap<>();
    private static final String[] STAGES={"입학과 첫 훈련","네 개의 흔적","아카데미 방어전","봉인의 진실","세 전선","마왕성 결전","엔딩 선택","캠페인 완료"};
    public static void show(ServerPlayer p,String title,String body,Entity npc,List<Option> options){
        String token=UUID.randomUUID().toString();
        SESSIONS.put(p.getUUID(),new Session(token,p.server.overworld().getGameTime()+12000,npc==null?null:npc.getUUID(),List.copyOf(options)));
        Packets.open(p,new Packets.View(token,title,body,options.stream().map(Option::label).toList()));
    }
    public static void clear(ServerPlayer p){SESSIONS.remove(p.getUUID());}
    public static void clearAll(){SESSIONS.clear();}
    public static void click(ServerPlayer p,String token,int index){
        var s=SESSIONS.get(p.getUUID());
        if(s==null||!s.token.equals(token))return;
        if(index==-1){clear(p);return;}
        if(!p.isAlive()||s.expires<p.server.overworld().getGameTime()||index<0||index>=s.options.size()){clear(p);return;}
        if(s.npc!=null){
            var entity=p.serverLevel().getEntity(s.npc);
            if(entity==null||!entity.isAlive()||p.distanceToSqr(entity)>49||!FantasiaMod.inCampaign(p)){clear(p);p.sendSystemMessage(Component.literal("NPC 가까이에서 다시 대화해 주세요."));return;}
        }
        // Consume before running: duplicate packets and stale exam buttons cannot award twice.
        clear(p);Playtime.activity(p);s.options.get(index).action.run();
    }
    public static String npcId(Entity entity){
        for(String tag:entity.getTags())if(tag.startsWith("fa_npc_")&&Content.MENUS.containsKey(tag.substring(7)))return tag.substring(7);
        return null;
    }
    public static void npc(ServerPlayer p,Entity entity){
        String id=npcId(entity);if(id==null||!FantasiaMod.inCampaign(p)||p.distanceToSqr(entity)>49)return;
        var spec=Content.MENUS.get(id);var opts=new ArrayList<Option>();
        if(id.equals("adeline")){
            opts.add(new Option(Progress.data(p).getBoolean("fantasia_exam_complete")?"검사 결과 · 재검사":"입학 검사 계속하기",()->Exams.show(p)));
        }
        Expeditions.addOptions(p,entity,id,opts);
        for(var a:spec.actions()){
            if(a.id()==2)continue;
            if(a.id()>=101&&a.id()<=110){
                int needed=a.id()<=104?1:a.id()==105?2:a.id()==106?3:a.id()<=109?4:5;
                if(Progress.score(p,"fa_stage")<needed)continue;
            }
            opts.add(new Option(a.label(),()->campaignAction(p,a.id())));
        }
        if(id.equals("kyle"))opts.add(new Option("기초 과정 확인",()->foundation(p)));
        if(id.equals("noah"))opts.add(new Option("마법 연구와 각인",()->Magic.menu(p,entity)));
        if(id.equals("headmaster")&&Progress.score(p,"fa_stage")==6){
            String[] endings={"봉인 재구축","마왕의 힘 소멸","마력 통제","진실의 결말"};
            for(int i=0;i<4;i++){int action=61+i;opts.add(new Option(endings[i],()->campaignAction(p,action)));}
        }
        Bonds.add(p,entity,id,opts);
        var npc=Content.NPCS.get(id);
        if(npc!=null&&npc.relation())opts.add(new Option("손에 든 아이템 선물",()->{gift(p,id);npc(p,entity);}));
        opts.add(new Option("현재 목표와 성장 기록",()->journal(p)));
        String body=spec.body();
        if(npc!=null&&npc.relation())body+="\n\n인연 "+Progress.data(p).getInt("fantasia_affection_"+id)+" / 100 · 선물은 30초 간격";
        show(p,spec.title(),body,entity,opts);
    }
    public static void campaignAction(ServerPlayer p,int action){
        if(action==64&&(!Expeditions.done(p,"buried_lab")||!Expeditions.done(p,"cult_hideout")||!Expeditions.done(p,"castle_memory")||Bonds.deepBonds(p)<2)){p.sendSystemMessage(Component.literal("진실의 결말에는 연구소·교수 구출·왕좌 기록과 두 명 이상의 깊은 인연이 필요합니다."));return;}
        if(action>=101&&action<=104&&!foundationComplete(p)){foundation(p);return;}
        String required=Expeditions.required(action);
        if(required!=null&&!Expeditions.done(p,required)){p.sendSystemMessage(Component.literal("먼저 안내 NPC의 원정을 완료하세요: "+Expeditions.chapter(required).title()));return;}
        // Only pre-authorized menu options call this; the datapack rechecks stage and location.
        Progress.command(p,"scoreboard players set @s fa_action "+action);
        Progress.command(p,"function fantasia:action");
    }
    public static void gift(ServerPlayer p,String id){
        var spec=Content.NPCS.get(id);if(spec==null||!spec.relation())return;
        var data=Progress.data(p);String key="fantasia_affection_"+id,time="fantasia_gift_time_"+id;
        int before=Math.clamp(data.getInt(key),0,100);long now=p.server.overworld().getGameTime();
        var held=p.getMainHandItem();
        if(held.isEmpty()||before>=100){p.sendSystemMessage(Component.literal("선물할 아이템을 주 손에 들어주세요. 인연이 최대라면 더 소비하지 않습니다."));return;}
        if(data.contains(time)&&now>=data.getLong(time)&&now-data.getLong(time)<600){p.sendSystemMessage(Component.literal("선물 후 30초가 지나야 다시 선물할 수 있습니다."));return;}
        int gain=net.minecraft.core.registries.BuiltInRegistries.ITEM.getKey(held.getItem()).toString().equals(spec.fav())?5:1;
        held.shrink(1);int after=Math.min(100,before+gain);data.putInt(key,after);data.putLong(time,now);p.containerMenu.broadcastChanges();
        if(after>=80)Progress.grant(p,"bond/"+id);
        p.sendSystemMessage(Component.literal(spec.name()+" 인연 +"+(after-before)+" ("+after+"/100)"));
    }
    public static boolean foundationComplete(ServerPlayer p){
        return List.of("target","enchant","alchemy","combat").stream().allMatch(id->Progress.has(p,"course/foundation/"+id));
    }
    public static void foundation(ServerPlayer p){
        String[] ids={"target","enchant","alchemy","combat"};
        String[] names={"표적 중심 명중", "책 마법부여", "포션 양조", "좀비·스켈레톤·거미 실전"};
        StringBuilder body=new StringBuilder("카일에게 훈련 장비와 선택 실습 재료를 받아주세요.\n\n");
        for(int i=0;i<ids.length;i++)body.append(Progress.has(p,"course/foundation/"+ids[i])?"[완료] ":"[진행] ").append(names[i]).append("\n");
        body.append("\n표적: 아카데미 동쪽 X 25 / Z 14 부근. 활로 중심을 맞히세요.\n마법부여실: X -21 / Z -20. 책·청금석·경험치를 사용합니다.\n연금실: X 21 / Z -20. 블레이즈 가루를 연료로 넣고 물병 → 네더 사마귀 → 설탕 순서로 양조한 뒤 완성된 병을 꺼내세요.\n실전: 카일의 기초 훈련에서 세 종류의 적을 제압합니다.\n\n입학 검사, 기초 과정, 아델린의 첫 원정을 마치면 네 지역 조사로 나갈 수 있습니다.");
        show(p,"아카데미 기초 과정",body.toString(),null,List.of(new Option("돌아가기",()->journal(p))));
    }
    public static void journal(ServerPlayer p){
        int stage=Math.clamp(Progress.score(p,"fa_stage"),0,7);
        String[] goals={"입학 검사 후 카일에게 장비를 받고 기초 훈련을 완료하세요.","광산·수로·숲·평원의 장치와 전투를 완료하세요. 아델린에게서 이동할 수 있습니다.","수도에서 에드릭과 함께 방어선을 지키세요.","봉인서고에서 서쪽 → 동쪽 → 중앙 기록을 조사하고 라헬에게 보고하세요.","북부·동부·남부 전선을 안정시키세요.","마왕성에서 헤론과 대화하고 왕좌로 진입하세요.","헤론에게 돌아가 마지막 결정을 내려주세요.","인연·다른 계통의 연구·선택 실습을 이어갈 수 있습니다."};
        String title=stage==0?"입학과 첫 훈련":STAGES[stage];
        var opts=new ArrayList<Option>();opts.add(new Option("입학 검사 · 내 정보",()->Exams.show(p)));
        Expeditions.journal(p,opts);
        opts.add(new Option("무기 숙련",()->Mastery.show(p)));
        opts.add(new Option("기초 과정",()->foundation(p)));
        show(p,title,goals[stage]+"\n\n"+Playtime.display(p),null,opts);
    }
    private Menus(){}
}
