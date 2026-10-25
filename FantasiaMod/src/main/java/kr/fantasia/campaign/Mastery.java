package kr.fantasia.campaign;

import net.minecraft.server.level.ServerPlayer;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.world.item.*;
import net.minecraft.world.entity.projectile.AbstractArrow;
import net.minecraft.world.entity.ai.attributes.*;
import net.minecraft.resources.ResourceLocation;
import net.neoforged.neoforge.event.entity.living.LivingDeathEvent;
import net.minecraft.network.chat.Component;
import java.util.*;

public final class Mastery {
    private static final ResourceLocation BONUS=ResourceLocation.fromNamespaceAndPath(FantasiaMod.ID,"weapon_training");
    public static String family(ItemStack item){
        String id=BuiltInRegistries.ITEM.getKey(item.getItem()).getPath();
        if(id.contains("greatsword")||id.contains("claymore"))return "greatsword";
        if(id.contains("dagger"))return "dagger";
        if(id.contains("spear")||id.contains("halberd")||item.getItem() instanceof TridentItem)return "spear";
        if(id.contains("hammer")||id.contains("mace"))return "hammer";
        if(item.getItem() instanceof CrossbowItem)return "crossbow";
        if(item.getItem() instanceof BowItem)return "bow";
        if(id.contains("staff"))return "staff";
        if(id.contains("spell_book")||id.contains("spellbook"))return "spellbook";
        if(item.getItem() instanceof AxeItem)return "axe";
        if(item.getItem() instanceof SwordItem)return "sword";
        return "";
    }
    public static void killed(LivingDeathEvent e){
        if(!(e.getSource().getEntity() instanceof ServerPlayer p)||!FantasiaMod.inCampaign(p))return;
        if(!e.getEntity().getTags().contains("fa_enemy")&&!e.getEntity().getTags().contains("fa_exp_enemy"))return;
        String family=family(p.getMainHandItem());
        if(e.getSource().getDirectEntity() instanceof AbstractArrow&&!(family.equals("bow")||family.equals("crossbow")))family="bow";
        if(family.isEmpty())return;
        award(p,family,1);
    }
    public static void award(ServerPlayer p,String family,int amount){
        if(!Content.EXAM.weapons().containsKey(family))return;
        var data=Progress.data(p);String key="mastery_"+family;int before=data.getInt(key);
        int gain=family.equals(data.getString("fantasia_weapon_main"))?amount*2:amount;
        int after=Math.min(1000,before+gain);data.putInt(key,after);
        if(before/25!=after/25)p.sendSystemMessage(Component.literal(Content.EXAM.weapons().get(family)+" 숙련 "+after+" / 1000"));
    }
    public static void tick(ServerPlayer p){
        if(p.tickCount%20!=0)return;
        String family=family(p.getMainHandItem());
        var attr=p.getAttribute(Attributes.ATTACK_DAMAGE);if(attr==null)return;
        attr.removeModifier(BONUS);
        if(!List.of("sword","greatsword","dagger","spear","axe","hammer").contains(family))return;
        double bonus=Math.min(2,Progress.data(p).getInt("mastery_"+family)/100.0);
        if(bonus>0)attr.addTransientModifier(new AttributeModifier(BONUS,bonus,AttributeModifier.Operation.ADD_VALUE));
    }
    public static void show(ServerPlayer p){
        StringBuilder text=new StringBuilder("무기 적성은 직업 제한이 아닙니다. 캠페인 적을 쓰러뜨리면 사용한 무기군의 숙련이 오릅니다. 추천 무기는 2배로 성장합니다.\n\n");
        Content.EXAM.weapons().forEach((id,label)->text.append(label).append(" · ").append(Progress.data(p).getInt("mastery_"+id)).append(" / 1000\n"));
        text.append("\n근접 무기는 숙련 100당 공격력 +1, 최대 +2. 원거리·마법 숙련은 성장 기록이며 별도의 피해 보너스는 아직 적용하지 않습니다.");
        Menus.show(p,"무기 숙련",text.toString(),null,List.of(new Menus.Option("돌아가기",()->Menus.journal(p))));
    }
    private Mastery(){}
}
