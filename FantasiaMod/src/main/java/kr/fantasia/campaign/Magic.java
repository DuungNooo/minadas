package kr.fantasia.campaign;

import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.entity.Entity;
import net.neoforged.fml.ModList;
import java.util.List;

public final class Magic {
    public static void menu(ServerPlayer p,Entity npc){
        if(!ModList.get().isLoaded("irons_spellbooks")){
            Menus.show(p,"마법 연구","Iron’s Spells ’n Spellbooks를 설치하면 연구와 주문 각인을 사용할 수 있습니다.",npc,List.of(new Menus.Option("돌아가기",()->Menus.npc(p,npc))));return;
        }
        IronCompat.menu(p,npc);
    }
    private Magic(){}
}
