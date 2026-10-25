package kr.fantasia.campaign;

import net.minecraft.nbt.CompoundTag;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.resources.ResourceLocation;
import java.util.*;

public final class Exams {
    private static final List<String> MILESTONES=List.of("registration","physical","mana","control","weapon","affinity","complete");
    public static void restart(ServerPlayer p){
        var d=Progress.data(p);
        for(var key:Content.STATS)d.putInt("fantasia_"+key,5);
        for(var key:Content.EXAM.schools().keySet())d.putInt("fantasia_aff_"+key,0);
        for(var key:Content.EXAM.weapons().keySet())d.putInt("fantasia_weapon_"+key,0);
        d.putString("fantasia_primary","");d.putString("fantasia_secondary","");d.putString("fantasia_weapon_main","");
        d.putInt("fantasia_exam_stage",0);d.putBoolean("fantasia_exam_started",true);d.putBoolean("fantasia_exam_complete",false);
        for(var key:MILESTONES)Progress.revoke(p,"exam/"+key);
        Progress.grant(p,"exam/registration");apply(p);show(p);
    }
    public static void show(ServerPlayer p){
        var d=Progress.data(p);
        if(!d.getBoolean("fantasia_exam_started")){restart(p);return;}
        if(d.getBoolean("fantasia_exam_complete")){result(p);return;}
        int stage=d.getInt("fantasia_exam_stage");
        if(stage<0||stage>=Content.EXAM.questions().size()){
            Menus.show(p,"검사 기록 확인","검사 기록이 올바르지 않습니다. 재검사를 누르면 검사만 다시 시작합니다.",null,
                List.of(new Menus.Option("검사 다시 시작",()->restart(p))));return;
        }
        var q=Content.EXAM.questions().get(stage);var options=new ArrayList<Menus.Option>();
        StringBuilder body=new StringBuilder(q.text()).append("\n\n");
        for(int i=0;i<q.choices().size();i++){
            int choice=i;body.append(i+1).append(". ").append(q.choices().get(i).text()).append("\n\n");
            options.add(new Menus.Option((i+1)+"번 선택",()->answer(p,stage,choice)));
        }
        Menus.show(p,"입학 검사 "+(stage+1)+" / 12 · "+q.title(),body.toString(),null,options);
    }
    private static void add(CompoundTag d,Map<String,Integer> values,String prefix){
        if(values!=null)values.forEach((k,v)->d.putInt(prefix+k,Math.clamp(d.getInt(prefix+k)+v,0,100)));
    }
    static List<String> ranked(CompoundTag d,String prefix,Collection<String> keys){
        return keys.stream().sorted(Comparator.comparingInt((String k)->d.getInt(prefix+k)).reversed()).toList();
    }
    public static void answer(ServerPlayer p,int expected,int choice){
        var d=Progress.data(p);int stage=d.getInt("fantasia_exam_stage");
        if(d.getBoolean("fantasia_exam_complete")||stage!=expected||stage<0||stage>=12||choice<0||choice>=3)return;
        var c=Content.EXAM.questions().get(stage).choices().get(choice);
        add(d,c.stat(),"fantasia_");add(d,c.affinity(),"fantasia_aff_");add(d,c.weapon(),"fantasia_weapon_");
        String milestone=switch(stage){case 1->"physical";case 2->"mana";case 3->"control";case 6->"weapon";case 10->"affinity";default->null;};
        if(milestone!=null)Progress.grant(p,"exam/"+milestone);
        d.putInt("fantasia_exam_stage",stage+1);
        if(stage==11){
            var schools=ranked(d,"fantasia_aff_",Content.EXAM.schools().keySet());
            d.putString("fantasia_primary",schools.get(0));d.putString("fantasia_secondary",schools.get(1));
            d.putString("fantasia_weapon_main",ranked(d,"fantasia_weapon_",Content.EXAM.weapons().keySet()).getFirst());
            d.putBoolean("fantasia_exam_complete",true);Progress.grant(p,"exam/complete");Progress.grant(p,schools.getFirst()+"_tier_1");apply(p);
        }
        show(p);
    }
    public static void apply(ServerPlayer p){
        var d=Progress.data(p);
        for(var k:Content.STATS)d.putInt("fantasia_"+k,Math.clamp(d.getInt("fantasia_"+k),0,100));
        double str=Math.max(0,d.getInt("fantasia_str")-5),vit=Math.max(0,d.getInt("fantasia_vit")-5),agi=Math.max(0,d.getInt("fantasia_agi")-5),mag=Math.max(0,d.getInt("fantasia_mag")-5),mnd=Math.max(0,d.getInt("fantasia_mnd")-5);
        p.getAttribute(Attributes.MAX_HEALTH).setBaseValue(20+vit*.5);
        p.getAttribute(Attributes.ATTACK_DAMAGE).setBaseValue(1+str*.12);
        p.getAttribute(Attributes.MOVEMENT_SPEED).setBaseValue(.1+agi*.001);
        p.setHealth(Math.min(p.getHealth(),p.getMaxHealth()));
        attribute(p,"max_mana",100+mag*5);attribute(p,"mana_regen",1+mnd*.05);attribute(p,"spell_power",1+mag*.01);
    }
    private static void attribute(ServerPlayer p,String id,double value){
        BuiltInRegistries.ATTRIBUTE.getHolder(ResourceLocation.parse("irons_spellbooks:"+id)).ifPresent(holder->{var a=p.getAttribute(holder);if(a!=null)a.setBaseValue(value);});
    }
    public static void result(ServerPlayer p){
        var d=Progress.data(p);StringBuilder body=new StringBuilder();
        for(var k:Content.STATS)body.append(k.toUpperCase()).append(" ").append(d.getInt("fantasia_"+k)).append("   ");
        body.append("\n\n주 적성: ").append(Content.EXAM.schools().getOrDefault(d.getString("fantasia_primary"),"검사 전"));
        body.append("\n보조 적성: ").append(Content.EXAM.schools().getOrDefault(d.getString("fantasia_secondary"),"검사 전"));
        body.append("\n추천 무기: ").append(Content.EXAM.weapons().getOrDefault(d.getString("fantasia_weapon_main"),"검사 전"));
        body.append("\n\n검사는 시작 방향입니다. 모든 무기와 다른 계통도 성장할 수 있습니다.\n카일에게 장비와 기초 훈련을 요청하세요.");
        Menus.show(p,"나의 검사 결과",body.toString(),null,List.of(new Menus.Option("재검사",()->confirm(p)),new Menus.Option("목표와 성장 기록",()->Menus.journal(p))));
    }
    public static void confirm(ServerPlayer p){Menus.show(p,"재검사","검사 점수와 적성을 다시 정합니다. 지역 진행·이미 해금한 연구·인연은 유지됩니다.",null,List.of(new Menus.Option("첫 문항부터 다시 검사",()->restart(p)),new Menus.Option("돌아가기",()->result(p))));}
    private Exams(){}
}
