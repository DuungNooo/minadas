package kr.fantasia.campaign;

import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.item.Items;
import java.util.*;

/** Research requires practice evidence, not merely a story boss flag. */
public final class Research {
    public static final Map<String,String> STARTERS=Map.of("fire","firebolt","ice","icicle","lightning","electrocute","nature","poison_arrow","holy","heal","ender","magic_missile","blood","blood_slash","evocation","fang_strike","void","planar_sight");
    public static int count(ServerPlayer p,String school,String type){return Progress.data(p).getInt("practice_"+school+"_"+type);}
    public static void record(ServerPlayer p,String school,String type){
        if(!FantasiaMod.inCampaign(p)||!Content.EXAM.schools().containsKey(school))return;
        var d=Progress.data(p);String key="practice_"+school+"_"+type;d.putInt(key,Math.min(10000,d.getInt(key)+1));
    }
    public static void menu(ServerPlayer p,Entity npc,String school){
        String label=Content.EXAM.schools().get(school);StringBuilder body=new StringBuilder(label+" 연구 기록\n\n");
        body.append("시전 ").append(count(p,school,"cast")).append(" · 명중 ").append(count(p,school,"damage")).append(" · 회복 ").append(count(p,school,"heal")).append(" · 이동 ").append(count(p,school,"move")).append(" · 소환 ").append(count(p,school,"summon")).append("\n\n");
        body.append("1단계: 입학 검사 + 첫 원정 완료\n2단계: 해당 계통 시전 12회 + 실제 효과 6회 + 네 지역 조사\n3단계: 시전 30회 + 실제 효과 18회 + 지하 연구소의 진실\n\n각 단계의 연구에는 자수정 조각 1개를 사용합니다. 원정 완료 보상으로 얻을 수 있습니다. 연구는 전투 외에도 이동·치료·소환으로 진행할 수 있습니다.");
        var opts=new ArrayList<Menus.Option>();for(int i=1;i<=3;i++){int tier=i;opts.add(new Menus.Option(i+"단계 연구 "+(Progress.has(p,school+"_tier_"+i)?"(완료)":""),()->{unlock(p,school,tier);menu(p,npc,school);}));}
        opts.add(new Menus.Option("주문 목록으로",()->IronCompat.menu(p,npc)));
        Menus.show(p,label+" 연구",body.toString(),npc,opts);
    }
    public static int effects(ServerPlayer p,String school){return count(p,school,"damage")+count(p,school,"heal")+count(p,school,"move")+count(p,school,"summon")+(school.equals("void")?count(p,school,"cast")/2:0);}
    private static void unlock(ServerPlayer p,String school,int tier){
        String gate=school+"_tier_"+tier;if(Progress.has(p,gate))return;
        boolean ready=Progress.has(p,"exam/complete")&&Expeditions.done(p,"blackout");
        if(tier>1)ready&=Progress.has(p,school+"_tier_"+(tier-1));
        if(tier==2)ready&=count(p,school,"cast")>=12&&effects(p,school)>=6&&Progress.score(p,"fa_stage")>=2;
        if(tier==3)ready&=count(p,school,"cast")>=30&&effects(p,school)>=18&&Expeditions.done(p,"buried_lab");
        if(!ready){tell(p,"연구 기록과 이야기 진행 조건을 먼저 충족하세요.");return;}
        for(int i=0;i<p.getInventory().getContainerSize();i++){
            var stack=p.getInventory().getItem(i);if(stack.is(Items.AMETHYST_SHARD)&&!stack.isEmpty()){
                stack.shrink(1);Progress.grant(p,gate);p.containerMenu.broadcastChanges();tell(p,"연구 완료: "+Content.EXAM.schools().get(school)+" "+tier+"단계");return;
            }
        }
        tell(p,"연구용 자수정 조각이 필요합니다. 원정에서 확보할 수 있습니다.");
    }
    public static String spellRequirement(ServerPlayer p,String id){
        var gate=Content.SPELLS.get(id);if(gate==null)return "등록되지 않은 주문입니다.";
        if(!Progress.has(p,gate))return "먼저 "+gate+" 연구를 완료하세요.";
        String school=gate.substring(0,gate.indexOf("_tier_")),spell=id.substring(id.indexOf(':')+1);
        if(spell.equals(STARTERS.get(school)))return null;
        int tier=Integer.parseInt(gate.substring(gate.length()-1));
        int casts= tier==1?3:tier==2?12:30;
        if(count(p,school,"cast")<casts)return "이 계통의 실전 시전 기록 "+casts+"회가 필요합니다.";
        // Spell-specific additional practice, shared across schools so builds never become hard class locks.
        String kind=(spell.contains("heal")||spell.contains("regeneration"))?"heal":(spell.contains("teleport")||spell.contains("step")||spell.contains("dash"))?"move":spell.contains("summon")?"summon":"";
        if(tier>=2&&!kind.isEmpty()){
            int total=Content.EXAM.schools().keySet().stream().mapToInt(s->count(p,s,kind)).sum();
            if(total<3)return "이 주문은 실제 "+Map.of("heal","회복","move","이동","summon","소환").get(kind)+" 실습 3회가 추가로 필요합니다.";
        }
        return null;
    }
    private static void tell(ServerPlayer p,String text){p.sendSystemMessage(net.minecraft.network.chat.Component.literal(text));}
    private Research(){}
}
