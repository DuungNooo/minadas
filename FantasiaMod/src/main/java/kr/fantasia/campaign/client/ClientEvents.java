package kr.fantasia.campaign.client;

import kr.fantasia.campaign.*;
import net.minecraft.client.Minecraft;
import net.minecraft.client.KeyMapping;
import net.neoforged.api.distmarker.Dist;
import net.neoforged.bus.api.SubscribeEvent;
import net.neoforged.fml.common.EventBusSubscriber;
import net.neoforged.fml.event.lifecycle.FMLClientSetupEvent;
import net.neoforged.neoforge.client.event.RegisterKeyMappingsEvent;
import net.neoforged.neoforge.client.event.ClientTickEvent;
import org.lwjgl.glfw.GLFW;

@EventBusSubscriber(modid=FantasiaMod.ID,bus=EventBusSubscriber.Bus.MOD,value=Dist.CLIENT)
public final class ClientEvents {
    static final KeyMapping JOURNAL=new KeyMapping("key.fantasia.journal",GLFW.GLFW_KEY_J,"key.categories.fantasia");
    @SubscribeEvent public static void setup(FMLClientSetupEvent e){e.enqueueWork(()->Packets.clientView=view->Minecraft.getInstance().setScreen(new DialogueScreen(view)));}
    @SubscribeEvent public static void keys(RegisterKeyMappingsEvent e){e.register(JOURNAL);}
    @EventBusSubscriber(modid=FantasiaMod.ID,value=Dist.CLIENT)
    public static final class Tick {
        @SubscribeEvent public static void tick(ClientTickEvent.Post e){
            var mc=Minecraft.getInstance();
            while(JOURNAL.consumeClick())if(mc.player!=null&&mc.screen==null)mc.player.connection.sendCommand("fantasia");
        }
    }
}
