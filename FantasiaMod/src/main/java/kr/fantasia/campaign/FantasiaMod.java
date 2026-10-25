package kr.fantasia.campaign;

import com.mojang.logging.LogUtils;
import net.minecraft.commands.Commands;
import net.minecraft.commands.arguments.EntityArgument;
import net.minecraft.server.level.ServerPlayer;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.network.chat.Component;
import net.neoforged.bus.api.IEventBus;
import net.neoforged.fml.common.Mod;
import net.neoforged.fml.ModList;
import net.neoforged.neoforge.common.NeoForge;
import net.neoforged.neoforge.event.RegisterCommandsEvent;
import net.neoforged.neoforge.event.entity.player.PlayerEvent;
import net.neoforged.neoforge.event.entity.player.PlayerInteractEvent;
import net.neoforged.neoforge.event.level.ExplosionEvent;
import net.neoforged.neoforge.event.tick.PlayerTickEvent;
import net.neoforged.neoforge.event.server.ServerStoppedEvent;
import org.slf4j.Logger;
import java.util.*;

@Mod(FantasiaMod.ID)
public final class FantasiaMod {
    public static final String ID="fantasia_campaign";
    public static final Logger LOGGER=LogUtils.getLogger();
    private final Map<UUID,Long> pendingLogin=new HashMap<>();
    public FantasiaMod(IEventBus bus){
        bus.addListener(Packets::register);
        NeoForge.EVENT_BUS.addListener(Mastery::killed);
        NeoForge.EVENT_BUS.addListener(this::login);
        NeoForge.EVENT_BUS.addListener(this::logout);
        NeoForge.EVENT_BUS.addListener(this::tick);
        NeoForge.EVENT_BUS.addListener(this::clonePlayer);
        NeoForge.EVENT_BUS.addListener(this::respawn);
        NeoForge.EVENT_BUS.addListener(this::interact);
        NeoForge.EVENT_BUS.addListener(this::interactSpecific);
        NeoForge.EVENT_BUS.addListener(this::commands);
        NeoForge.EVENT_BUS.addListener(this::explosion);
        NeoForge.EVENT_BUS.addListener(this::stopped);
        NeoForge.EVENT_BUS.addListener(this::entityLoaded);
        if(ModList.get().isLoaded("irons_spellbooks"))IronCompat.register();
    }
    public static boolean inCampaign(net.minecraft.world.entity.Entity p){return p.level().dimension().location().toString().equals("fantasia:campaign");}
    private void entityLoaded(net.neoforged.neoforge.event.entity.EntityJoinLevelEvent e){
        if(e.loadedFromDisk()&&(e.getEntity().getTags().contains("fa_exp_enemy")||e.getEntity().getTags().contains("fa_exp_escort")))e.setCanceled(true);
    }
    private void login(PlayerEvent.PlayerLoggedInEvent e){if(e.getEntity() instanceof ServerPlayer p){Progress.migrate(p);pendingLogin.put(p.getUUID(),p.server.overworld().getGameTime()+40);}}
    private void logout(PlayerEvent.PlayerLoggedOutEvent e){if(e.getEntity() instanceof ServerPlayer p){pendingLogin.remove(p.getUUID());Menus.clear(p);Expeditions.abort(p);Playtime.clear(p);}}
    private void stopped(ServerStoppedEvent e){pendingLogin.clear();Menus.clearAll();Expeditions.clear();Playtime.clearAll();}
    private void clonePlayer(PlayerEvent.Clone e){Progress.copy(e.getOriginal(),e.getEntity());}
    private void respawn(PlayerEvent.PlayerRespawnEvent e){if(e.getEntity() instanceof ServerPlayer p){Menus.clear(p);if(Progress.data(p).getBoolean("fantasia_exam_started"))Exams.apply(p);}}
    private void tick(PlayerTickEvent.Post e){
        if(!(e.getEntity() instanceof ServerPlayer p))return;
        Expeditions.tick(p);Mastery.tick(p);Playtime.tick(p);
        var due=pendingLogin.get(p.getUUID());
        if(due==null||p.server.overworld().getGameTime()<due||!p.getTags().contains("fa_joined"))return;
        pendingLogin.remove(p.getUUID());
        if(Progress.data(p).getBoolean("fantasia_exam_complete"))Exams.apply(p);else Exams.show(p);
    }
    private void interact(PlayerInteractEvent.EntityInteract e){handle(e,e.getTarget());}
    private void interactSpecific(PlayerInteractEvent.EntityInteractSpecific e){handle(e,e.getTarget());}
    private void handle(PlayerInteractEvent e,net.minecraft.world.entity.Entity target){
        if(!inCampaign(target)||(Menus.npcId(target)==null&&!Expeditions.station(target)&&!target.getTags().contains("fa_exp_escort")))return;
        // Both interaction routes are canceled before Villager#mobInteract can open trading.
        if(e instanceof PlayerInteractEvent.EntityInteract interaction){interaction.setCanceled(true);interaction.setCancellationResult(InteractionResult.SUCCESS);}
        if(e instanceof PlayerInteractEvent.EntityInteractSpecific interaction){interaction.setCanceled(true);interaction.setCancellationResult(InteractionResult.SUCCESS);}
        if(e.getHand()==InteractionHand.MAIN_HAND&&e.getEntity() instanceof ServerPlayer p){
            if(Expeditions.station(target))Expeditions.interact(p,target);else Menus.npc(p,target);
        }
    }
    private void explosion(ExplosionEvent.Detonate e){if(e.getLevel().dimension().location().toString().equals("fantasia:campaign"))e.getAffectedBlocks().clear();}
    private void commands(RegisterCommandsEvent e){
        e.getDispatcher().register(Commands.literal("fantasia").executes(c->{Menus.journal(c.getSource().getPlayerOrException());return 1;})
            .then(Commands.literal("exam").executes(c->{Exams.show(c.getSource().getPlayerOrException());return 1;})
                .then(Commands.literal("restart").executes(c->{Exams.confirm(c.getSource().getPlayerOrException());return 1;})))
            .then(Commands.literal("restart").requires(s->s.hasPermission(2))
                .then(Commands.argument("player",EntityArgument.player()).executes(c->{Exams.restart(EntityArgument.getPlayer(c,"player"));c.getSource().sendSuccess(()->Component.literal("입학 검사를 다시 시작했습니다."),true);return 1;}))));
        e.getDispatcher().register(Commands.literal("fantasia_admin").requires(s->s.hasPermission(2))
            .then(Commands.literal("restart").then(Commands.argument("player",EntityArgument.player()).executes(c->{Exams.restart(EntityArgument.getPlayer(c,"player"));c.getSource().sendSuccess(()->Component.literal("재검사를 시작했습니다. 지역 진행과 연구는 유지됩니다."),true);return 1;}))));
        e.getDispatcher().register(Commands.literal("fantasia_exam").executes(c->{Exams.show(c.getSource().getPlayerOrException());return 1;})
            .then(Commands.literal("resume").executes(c->{Exams.show(c.getSource().getPlayerOrException());return 1;}))
            .then(Commands.literal("result").executes(c->{Exams.result(c.getSource().getPlayerOrException());return 1;})));
        e.getDispatcher().register(Commands.literal("fantasia_stats").executes(c->{Exams.result(c.getSource().getPlayerOrException());return 1;}));
    }
}
