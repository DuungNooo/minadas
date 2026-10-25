package kr.fantasia.campaign;

import net.minecraft.network.RegistryFriendlyByteBuf;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.network.protocol.common.custom.CustomPacketPayload;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.server.level.ServerPlayer;
import net.neoforged.neoforge.network.event.RegisterPayloadHandlersEvent;
import net.neoforged.neoforge.network.PacketDistributor;
import java.util.*;
import java.util.function.Consumer;

public final class Packets {
    public record View(String token,String title,String body,List<String> buttons) {}
    // Client installs this handler only on the physical client. Common classes never reference Minecraft.
    public static Consumer<View> clientView = view -> {};
    public record Open(String json) implements CustomPacketPayload {
        public static final Type<Open> TYPE=new Type<>(ResourceLocation.fromNamespaceAndPath(FantasiaMod.ID,"open"));
        public static final StreamCodec<RegistryFriendlyByteBuf,Open> CODEC=StreamCodec.of((b,p)->b.writeUtf(p.json,32767),b->new Open(b.readUtf(32767)));
        public Type<? extends CustomPacketPayload> type(){return TYPE;}
    }
    public record Click(String token,int index) implements CustomPacketPayload {
        public static final Type<Click> TYPE=new Type<>(ResourceLocation.fromNamespaceAndPath(FantasiaMod.ID,"click"));
        public static final StreamCodec<RegistryFriendlyByteBuf,Click> CODEC=StreamCodec.of((b,p)->{b.writeUtf(p.token,36);b.writeVarInt(p.index);},b->new Click(b.readUtf(36),b.readVarInt()));
        public Type<? extends CustomPacketPayload> type(){return TYPE;}
    }
    public static void register(RegisterPayloadHandlersEvent event){
        var registrar=event.registrar("1");
        registrar.playToClient(Open.TYPE,Open.CODEC,(p,c)->c.enqueueWork(()->clientView.accept(Content.GSON.fromJson(p.json,View.class))));
        registrar.playToServer(Click.TYPE,Click.CODEC,(p,c)->c.enqueueWork(()->{if(c.player() instanceof ServerPlayer player) Menus.click(player,p.token,p.index);}));
    }
    public static void open(ServerPlayer player,View view){PacketDistributor.sendToPlayer(player,new Open(Content.GSON.toJson(view)));}
    private Packets(){}
}
