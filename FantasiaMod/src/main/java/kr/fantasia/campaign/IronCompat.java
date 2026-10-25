package kr.fantasia.campaign;

import io.redspace.ironsspellbooks.api.events.*;
import io.redspace.ironsspellbooks.api.registry.SpellRegistry;
import io.redspace.ironsspellbooks.api.spells.ISpellContainer;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.item.ItemStack;
import net.minecraft.network.chat.Component;
import net.neoforged.neoforge.common.NeoForge;
import java.util.*;

public final class IronCompat {
    public static void register(){
        NeoForge.EVENT_BUS.addListener(IronCompat::cast);
        NeoForge.EVENT_BUS.addListener(IronCompat::casted);
        NeoForge.EVENT_BUS.addListener(IronCompat::damage);
        NeoForge.EVENT_BUS.addListener(IronCompat::heal);
        NeoForge.EVENT_BUS.addListener(IronCompat::teleport);
        NeoForge.EVENT_BUS.addListener(IronCompat::summon);
    }
    private static String school(String id){String gate=Content.SPELLS.get(id);return gate==null?"":gate.substring(0,gate.indexOf("_tier_"));}
    private static void casted(SpellOnCastEvent e){if(e.getEntity() instanceof ServerPlayer p){Research.record(p,school(e.getSpellId()),"cast");String weapon=Mastery.family(p.getMainHandItem());Mastery.award(p,weapon.equals("sword")?"hybrid":weapon.equals("staff")?"staff":"spellbook",1);}}
    private static void damage(SpellDamageEvent e){
        if(e.isCanceled()||e.getAmount()<=0||(!e.getEntity().getTags().contains("fa_enemy")&&!e.getEntity().getTags().contains("fa_exp_enemy")))return;
        if(e.getSpellDamageSource().getEntity() instanceof ServerPlayer p){
            String school=school(e.getSpellDamageSource().spell().getSpellId());
            // Continuous beams may cause many events; count at most one proof per second per school.
            var data=Progress.data(p);long now=p.server.overworld().getGameTime();String key="proof_time_"+school;
            if(!data.contains(key)||now-data.getLong(key)>=20){data.putLong(key,now);Research.record(p,school,"damage");}
        }
    }
    private static void heal(SpellHealEvent e){if(e.getEntity() instanceof ServerPlayer p&&e.getHealAmount()>0&&e.getTargetEntity().getHealth()<e.getTargetEntity().getMaxHealth())Research.record(p,"holy","heal");}
    private static void teleport(SpellTeleportEvent e){if(!e.isCanceled()&&e.getEntity() instanceof ServerPlayer p&&p.position().distanceToSqr(new net.minecraft.world.phys.Vec3(e.getTargetX(),e.getTargetY(),e.getTargetZ()))>=9)Research.record(p,school(e.getSpell().getSpellId()),"move");}
    private static void summon(SpellSummonEvent<?> e){if(e.getCaster() instanceof ServerPlayer p)Research.record(p,school(e.getSpellId().toString()),"summon");}
    private static void cast(SpellPreCastEvent e){
        if(!(e.getEntity() instanceof ServerPlayer p))return;
        String id=e.getSpellId();String gate=Content.SPELLS.get(id);
        boolean destructive=id.equals("irons_spellbooks:touch_dig")||id.equals("irons_spellbooks:spectral_hammer");
        if((destructive&&(FantasiaMod.inCampaign(p)||!Progress.has(p,"map_breaking_magic")))||(gate!=null&&Research.spellRequirement(p,id)!=null)){
            e.setCanceled(true);p.displayClientMessage(Component.literal("해당 주문의 연구가 필요하거나 이 지역에서 사용할 수 없는 주문입니다."),true);
        }
    }
    public static void menu(ServerPlayer p,Entity npc){
        if(!Progress.has(p,"exam/complete")){
            Menus.show(p,"연구 준비","입학 검사를 먼저 완료하세요.",npc,List.of(new Menus.Option("검사 시작",()->Exams.show(p))));return;
        }
        var opts=new ArrayList<Menus.Option>();opts.add(new Menus.Option("연구용 철 마법서 받기",()->{book(p);menu(p,npc);}));
        Content.EXAM.schools().forEach((key,label)->opts.add(new Menus.Option(label+" 연구",()->school(p,npc,key,label))));
        Menus.show(p,"노아의 마법 연구","연구를 해금한 뒤 철 마법서를 주 손에 들고 주문을 각인하세요. 연구용 책에는 6개의 주문을 넣을 수 있습니다.",npc,opts);
    }
    private static void book(ServerPlayer p){
        var d=Progress.data(p);long now=p.server.overworld().getGameTime();
        if(d.contains("fantasia_book_time")&&now>=d.getLong("fantasia_book_time")&&now-d.getLong("fantasia_book_time")<1200){message(p,"마법서는 1분마다 받을 수 있습니다.");return;}
        var item=BuiltInRegistries.ITEM.get(ResourceLocation.parse("irons_spellbooks:iron_spell_book"));
        var stack=new ItemStack(item);if(stack.isEmpty()){message(p,"현재 Iron’s 버전에 연구용 책이 없습니다.");return;}
        ISpellContainer.set(stack,ISpellContainer.create(6,true,true));
        if(!p.getInventory().add(stack))p.drop(stack,false);
        d.putLong("fantasia_book_time",now);
    }
    private static void school(ServerPlayer p,Entity npc,String school,String label){
        var opts=new ArrayList<Menus.Option>();
        opts.add(new Menus.Option("연구 승급 · 실습 기록",()->Research.menu(p,npc,school)));
        Content.SPELLS.forEach((id,gate)->{
            if(!gate.startsWith(school+"_tier_")||!Progress.has(p,gate)||id.endsWith(":touch_dig")||id.endsWith(":spectral_hammer"))return;
            var spell=SpellRegistry.REGISTRY.get(ResourceLocation.parse(id));
            if(spell==null||spell==SpellRegistry.none())return;
            // Client resolves translation keys, so buttons remain localized on a dedicated server.
            opts.add(new Menus.Option("translate:spell.irons_spellbooks."+id.split(":")[1],()->{learn(p,id);school(p,npc,school,label);}));
        });
        opts.add(new Menus.Option("다른 계통",()->menu(p,npc)));
        Menus.show(p,label+" 주문 각인","각인은 연구용 철 마법서를 주 손에 들어야 합니다. 해금된 주문만 표시됩니다.",npc,opts);
    }
    private static void learn(ServerPlayer p,String id){
        var gate=Content.SPELLS.get(id);if(gate==null||!Progress.has(p,gate))return;
        String requirement=Research.spellRequirement(p,id);if(requirement!=null){message(p,requirement);return;}
        var held=p.getMainHandItem();if(!BuiltInRegistries.ITEM.getKey(held.getItem()).toString().equals("irons_spellbooks:iron_spell_book")){message(p,"연구용 철 마법서를 주 손에 들어주세요.");return;}
        var spell=SpellRegistry.REGISTRY.get(ResourceLocation.parse(id));if(spell==null||spell==SpellRegistry.none())return;
        var current=ISpellContainer.getOrCreate(held);if(current.getIndexForSpell(spell)>=0){message(p,"이미 각인한 주문입니다.");return;}
        var mutable=current.mutableCopy();if(!mutable.addSpell(spell,1,false)){message(p,"책의 슬롯이 가득 찼습니다.");return;}
        ISpellContainer.set(held,mutable.toImmutable());p.containerMenu.broadcastChanges();message(p,"주문을 각인했습니다. 마법서를 장착하고 Iron’s 시전 키를 사용하세요.");
    }
    private static void message(ServerPlayer p,String message){p.sendSystemMessage(Component.literal(message));}
    private IronCompat(){}
}
