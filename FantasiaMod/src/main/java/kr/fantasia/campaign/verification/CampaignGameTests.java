package kr.fantasia.campaign.verification;

import com.mojang.authlib.GameProfile;
import kr.fantasia.campaign.*;
import net.minecraft.gametest.framework.*;
import net.minecraft.resources.ResourceKey;
import net.minecraft.resources.ResourceLocation;
import net.minecraft.core.registries.Registries;
import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.entity.EntityType;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.phys.Vec3;
import net.minecraft.server.level.ServerPlayer;
import net.neoforged.neoforge.common.NeoForge;
import net.neoforged.neoforge.common.util.FakePlayerFactory;
import net.neoforged.neoforge.event.entity.player.PlayerInteractEvent;
import net.neoforged.neoforge.gametest.GameTestHolder;
import net.neoforged.neoforge.gametest.PrefixGameTestTemplate;
import java.util.UUID;

@GameTestHolder(FantasiaMod.ID)
@PrefixGameTestTemplate(false)
public final class CampaignGameTests {
    private static final java.util.Map<UUID,Packets.View> VIEWS=new java.util.HashMap<>();
    private static ServerPlayer player(GameTestHelper h,String name){
        var level=h.getLevel().getServer().getLevel(ResourceKey.create(Registries.DIMENSION,ResourceLocation.parse("fantasia:campaign")));
        h.assertTrue(level!=null,"Campaign dimension is registered");
        var profile=new GameProfile(UUID.nameUUIDFromBytes(name.getBytes(java.nio.charset.StandardCharsets.UTF_8)),name);
        var p=new ServerPlayer(level.getServer(),level,profile,net.minecraft.server.level.ClientInformation.createDefault());
        // Real ServerPlayer/advancement logic, with network output discarded. NeoForge intentionally denies advancements to FakePlayer.
        p.connection=new net.minecraft.server.network.ServerGamePacketListenerImpl(level.getServer(),
            new net.minecraft.network.Connection(net.minecraft.network.protocol.PacketFlow.SERVERBOUND),p,
            net.minecraft.server.network.CommonListenerCookie.createInitial(profile,false)){
                @Override public void send(net.minecraft.network.protocol.Packet<?> packet){
                    if(packet instanceof net.minecraft.network.protocol.common.ClientboundCustomPayloadPacket custom&&custom.payload() instanceof Packets.Open open)
                        VIEWS.put(p.getUUID(),Content.GSON.fromJson(open.json(),Packets.View.class));
                }
            };
        p.setPos(0,65,0);return p;
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void exam_and_restart(GameTestHelper h){
        var p=player(h,"ExamTester");Exams.restart(p);
        for(int i=0;i<12;i++)Exams.answer(p,i,0);
        h.assertTrue(Progress.data(p).getBoolean("fantasia_exam_complete"),"12 answers finish the exam");
        h.assertTrue(Progress.has(p,"exam/complete"),"completion advancement granted");
        Progress.grant(p,"fire_tier_2");Progress.data(p).putInt("exp_blackout",6);Progress.data(p).putInt("fantasia_affection_adeline",42);
        Exams.restart(p);
        h.assertTrue(Progress.data(p).getInt("fantasia_exam_stage")==0,"restart returns to first question");
        h.assertTrue(!Progress.has(p,"exam/complete"),"exam milestone revoked");
        h.assertTrue(Progress.has(p,"fire_tier_2"),"earned research preserved");
        h.assertTrue(Progress.data(p).getInt("exp_blackout")==6,"expedition preserved");
        h.assertTrue(Progress.data(p).getInt("fantasia_affection_adeline")==42,"bond preserved");
        h.assertTrue(p.getAttribute(Attributes.MAX_HEALTH).getBaseValue()==20,"exam attributes reset");h.succeed();
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void stale_answers(GameTestHelper h){
        var p=player(h,"ReplayTester");Exams.restart(p);Exams.answer(p,0,0);
        int strength=Progress.data(p).getInt("fantasia_str");Exams.answer(p,0,0);Exams.answer(p,1,99);
        h.assertTrue(Progress.data(p).getInt("fantasia_exam_stage")==1,"stale and invalid answers ignored");
        h.assertTrue(Progress.data(p).getInt("fantasia_str")==strength,"no duplicate rewards");h.succeed();
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void villager_trade_is_canceled(GameTestHelper h){
        var p=player(h,"NpcTester");var v=EntityType.VILLAGER.create(p.serverLevel());v.setPos(0,65,1);v.addTag("fa_npc");v.addTag("fa_npc_adeline");
        var normal=new PlayerInteractEvent.EntityInteract(p,InteractionHand.MAIN_HAND,v);NeoForge.EVENT_BUS.post(normal);
        h.assertTrue(normal.isCanceled()&&normal.getCancellationResult()==InteractionResult.SUCCESS,"normal NPC use consumes vanilla trading");
        var specific=new PlayerInteractEvent.EntityInteractSpecific(p,InteractionHand.MAIN_HAND,v,new Vec3(0,1,0));NeoForge.EVENT_BUS.post(specific);
        h.assertTrue(specific.isCanceled(),"specific NPC interaction also cancels trading");
        var ordinary=EntityType.VILLAGER.create(p.serverLevel());ordinary.setPos(0,65,1);
        var event=new PlayerInteractEvent.EntityInteract(p,InteractionHand.MAIN_HAND,ordinary);NeoForge.EVENT_BUS.post(event);
        h.assertTrue(!event.isCanceled(),"ordinary villagers keep trading");h.succeed();
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void restart_command_registration(GameTestHelper h){
        var p=player(h,"CommandTester");var dispatcher=p.server.getCommands().getDispatcher();
        try{
            int result=dispatcher.execute("fantasia_admin restart @s",p.createCommandSourceStack().withPermission(2));
            h.assertTrue(result==1&&Progress.data(p).getBoolean("fantasia_exam_started"),"legacy restart command executes through Brigadier");
            boolean denied=false;try{dispatcher.execute("fantasia_admin restart @s",p.createCommandSourceStack().withPermission(0));}catch(Exception expected){denied=true;}
            h.assertTrue(denied,"admin command requires permission");
            h.assertTrue(dispatcher.execute("fantasia exam restart",p.createCommandSourceStack().withPermission(0))==1,"self retake confirmation works without OP");
        }catch(Exception e){throw new RuntimeException(e);}h.succeed();
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void single_use_menu_token(GameTestHelper h){
        var p=player(h,"MenuTester");var used=new java.util.concurrent.atomic.AtomicInteger();
        Menus.show(p,"Test","Test",null,java.util.List.of(new Menus.Option("Accept",used::incrementAndGet)));
        var view=VIEWS.get(p.getUUID());h.assertTrue(view!=null,"server emits typed screen payload");
        Menus.click(p,"forged",0);h.assertTrue(used.get()==0,"forged token rejected");
        Menus.click(p,view.token(),0);Menus.click(p,view.token(),0);
        h.assertTrue(used.get()==1,"a menu choice can be consumed only once");h.succeed();
    }
    @GameTest(template="test_empty",timeoutTicks=6000)
    public static void expedition_record_and_order(GameTestHelper h){
        var p=player(h,"ExpTester");var c=Expeditions.chapter("blackout");Progress.data(p).putInt("exp_blackout",0);
        var step=c.steps().getFirst();p.setPos(step.x(),65,step.z()+1);
        int chunkX=step.x()>>4,chunkZ=step.z()>>4;
        boolean alreadyForced=p.serverLevel().getForcedChunks().contains(net.minecraft.world.level.ChunkPos.asLong(chunkX,chunkZ));
        p.serverLevel().setChunkForced(chunkX,chunkZ,true);
        h.startSequence().thenWaitUntil(()->h.assertTrue(p.serverLevel().isPositionEntityTicking(new net.minecraft.core.BlockPos(step.x(),65,step.z())),"waiting for active expedition chunk")).thenExecute(()->{
            var station=EntityType.INTERACTION.create(p.serverLevel());station.moveTo(step.x(),65,step.z(),0,0);station.addTag("fa_exp_station");station.addTag("fa_exp_blackout_0");p.serverLevel().addFreshEntity(station);
            h.assertTrue(p.serverLevel().getEntity(station.getUUID())!=null,"station exists in an active chunk");
            Expeditions.interact(p,station);var view=VIEWS.get(p.getUUID());
            h.assertTrue(view!=null&&view.title().equals(step.title()),"world marker opens current authored objective");
            Menus.click(p,view.token(),0);
            h.assertTrue(Expeditions.progress(p,c)==1,"confirming evidence advances exactly once");
            Menus.click(p,view.token(),0);Expeditions.interact(p,station);
            h.assertTrue(Expeditions.progress(p,c)==1,"old marker and stale token cannot advance next step");station.discard();
            if(!alreadyForced)p.serverLevel().setChunkForced(chunkX,chunkZ,false);
        }).thenSucceed();
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void foundation_requires_real_milestones(GameTestHelper h){
        var p=player(h,"CourseTester");
        for(var id:java.util.List.of("target","enchant","alchemy","combat"))Progress.revoke(p,"course/foundation/"+id);
        h.assertTrue(!Menus.foundationComplete(p),"foundation cannot be skipped");
        Progress.grant(p,"course/foundation/target");Progress.grant(p,"course/foundation/enchant");Progress.grant(p,"course/foundation/alchemy");
        h.assertTrue(!Menus.foundationComplete(p),"combat is also required");
        Progress.grant(p,"course/foundation/combat");h.assertTrue(Menus.foundationComplete(p),"all four real advancement milestones unlock field study");h.succeed();
    }
    @GameTest(template="test_empty",timeoutTicks=2400)
    public static void maps_finish_with_walkable_rooms(GameTestHelper h){
        var server=h.getLevel().getServer();
        h.succeedWhen(()->{
            var level=server.getLevel(ResourceKey.create(Registries.DIMENSION,ResourceLocation.parse("fantasia:campaign")));
            h.assertTrue(level!=null,"campaign level exists");
            var board=server.getScoreboard();var obj=board.getObjective("fa_world");h.assertTrue(obj!=null,"world objective exists");
            for(String name:java.util.List.of("#ready","#exp_ready")){
                var score=board.getPlayerScoreInfo(net.minecraft.world.scores.ScoreHolder.forNameOnly(name),obj);
                h.assertTrue(score!=null&&score.value()==1,"waiting for map construction: "+name);
            }
            int[][] areas={{0,0},{160,0},{0,160},{-160,0},{0,-160},{160,160},{-160,160},{-160,-160},{160,-160},{320,0},{320,160}};
            for(var a:areas){
                level.getChunkAt(new net.minecraft.core.BlockPos(a[0],64,a[1]-20));
                h.assertTrue(!level.getBlockState(new net.minecraft.core.BlockPos(a[0],64,a[1]-20)).isAir(),"main-map arrival has a floor");
                h.assertTrue(level.getBlockState(new net.minecraft.core.BlockPos(a[0],65,a[1]-20)).isAir(),"main-map arrival has headroom");
            }
            for(var c:Expeditions.CATALOG.chapters())for(var step:c.steps()){
                var floor=new net.minecraft.core.BlockPos(step.x(),64,step.z()+9);level.getChunkAt(floor);
                h.assertTrue(!level.getBlockState(floor).isAir(),"expedition checkpoint floor: "+c.id());
                h.assertTrue(level.getBlockState(floor.above()).isAir(),"expedition checkpoint headroom: "+c.id());
            }
        });
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void old_kubejs_progress_migrates_once(GameTestHelper h){
        var p=player(h,"MigrationTester");var d=Progress.data(p);d.remove("migrated");
        var legacy=new net.minecraft.nbt.CompoundTag();legacy.putInt("fantasia_str",23);legacy.putBoolean("fantasia_exam_complete",true);legacy.putString("fantasia_primary","fire");legacy.putString("unrelated","do not import");
        var root=new net.minecraft.nbt.CompoundTag();root.put("KubeJSPersistentData",legacy);
        var file=p.server.getWorldPath(net.minecraft.world.level.storage.LevelResource.PLAYER_DATA_DIR).resolve(p.getUUID()+".dat");
        try{
            java.nio.file.Files.createDirectories(file.getParent());net.minecraft.nbt.NbtIo.writeCompressed(root,file);Progress.migrate(p);
            h.assertTrue(d.getInt("fantasia_str")==23&&d.getBoolean("fantasia_exam_complete"),"legacy score and completion imported from actual player NBT");
            h.assertTrue(d.getString("fantasia_primary").equals("fire")&&!d.contains("unrelated"),"only campaign data is imported");
            d.putInt("fantasia_str",30);Progress.migrate(p);h.assertTrue(d.getInt("fantasia_str")==30,"migration never overwrites later changes");java.nio.file.Files.deleteIfExists(file);
        }catch(java.io.IOException e){throw new RuntimeException(e);}h.succeed();
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void typed_packet_round_trip(GameTestHelper h){
        var p=player(h,"PacketTester");var buffer=new net.minecraft.network.RegistryFriendlyByteBuf(io.netty.buffer.Unpooled.buffer(),p.registryAccess());
        try{
            var view=new Packets.View("token","검사 화면","문항과 설명",java.util.List.of("첫 번째","두 번째"));
            var open=new Packets.Open(Content.GSON.toJson(view));Packets.Open.CODEC.encode(buffer,open);
            var decoded=Content.GSON.fromJson(Packets.Open.CODEC.decode(buffer).json(),Packets.View.class);
            h.assertTrue(decoded.equals(view),"Korean screen content and choices survive network encoding");
            buffer.clear();var click=new Packets.Click("12345678-1234-1234-1234-123456789012",2);Packets.Click.CODEC.encode(buffer,click);
            h.assertTrue(Packets.Click.CODEC.decode(buffer).equals(click),"menu tokens and choice indexes round trip");
        }finally{buffer.release();}h.succeed();
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void irons_native_research_gate(GameTestHelper h){
        h.assertTrue(net.neoforged.fml.ModList.get().isLoaded("irons_spellbooks"),"this integration suite requires the pinned Iron's mod");
        var p=player(h,"IronGateTester");
        var spell=io.redspace.ironsspellbooks.api.registry.SpellRegistry.REGISTRY.get(ResourceLocation.parse("irons_spellbooks:firebolt"));
        h.assertTrue(spell!=null&&spell!=io.redspace.ironsspellbooks.api.registry.SpellRegistry.none(),"real spell registry resolves the starter");
        Progress.revoke(p,"fire_tier_1");
        var locked=new io.redspace.ironsspellbooks.api.events.SpellPreCastEvent(p,spell.getSpellId(),1,spell.getSchoolType(),io.redspace.ironsspellbooks.api.spells.CastSource.SPELLBOOK);
        NeoForge.EVENT_BUS.post(locked);h.assertTrue(locked.isCanceled(),"native casting event blocks unresearched spells");
        Progress.grant(p,"fire_tier_1");
        var allowed=new io.redspace.ironsspellbooks.api.events.SpellPreCastEvent(p,spell.getSpellId(),1,spell.getSchoolType(),io.redspace.ironsspellbooks.api.spells.CastSource.SPELLBOOK);
        NeoForge.EVENT_BUS.post(allowed);h.assertTrue(!allowed.isCanceled(),"researched starter is castable");
        int before=Research.count(p,"fire","cast");
        NeoForge.EVENT_BUS.post(new io.redspace.ironsspellbooks.api.events.SpellOnCastEvent(p,spell.getSpellId(),1,1,spell.getSchoolType(),io.redspace.ironsspellbooks.api.spells.CastSource.SPELLBOOK));
        h.assertTrue(Research.count(p,"fire","cast")==before+1,"successful cast event records school practice");
        var hammer=io.redspace.ironsspellbooks.api.registry.SpellRegistry.REGISTRY.get(ResourceLocation.parse("irons_spellbooks:spectral_hammer"));
        var destructive=new io.redspace.ironsspellbooks.api.events.SpellPreCastEvent(p,hammer.getSpellId(),1,hammer.getSchoolType(),io.redspace.ironsspellbooks.api.spells.CastSource.COMMAND);
        NeoForge.EVENT_BUS.post(destructive);h.assertTrue(destructive.isCanceled(),"terrain-breaking spell stays blocked in the campaign");h.succeed();
    }
    @GameTest(template="test_empty",timeoutTicks=6000)
    public static void irons_book_and_inscription(GameTestHelper h){
        var p=player(h,"IronBookTester");Progress.grant(p,"exam/complete");Progress.grant(p,"fire_tier_1");Progress.data(p).remove("fantasia_book_time");
        p.getInventory().clearContent();p.serverLevel().setChunkForced(0,0,true);
        h.startSequence().thenWaitUntil(()->h.assertTrue(p.serverLevel().isPositionEntityTicking(new net.minecraft.core.BlockPos(0,65,1)),"waiting for active academy chunk")).thenExecute(()->{
            var npc=EntityType.VILLAGER.create(p.serverLevel());npc.setPos(0,65,1);npc.addTag("fa_npc_noah");npc.addTag("fa_npc");p.serverLevel().addFreshEntity(npc);
            IronCompat.menu(p,npc);var first=VIEWS.get(p.getUUID());Menus.click(p,first.token(),0);
            var book=p.getMainHandItem();
            h.assertTrue(net.minecraft.core.registries.BuiltInRegistries.ITEM.getKey(book.getItem()).toString().equals("irons_spellbooks:iron_spell_book"),"book menu gives an actual Iron's spellbook");
            var schoolMenu=VIEWS.get(p.getUUID());int school=schoolMenu.buttons().indexOf(Content.EXAM.schools().get("fire")+" 연구");h.assertTrue(school>=0,"fire school is present in screen");
            Menus.click(p,schoolMenu.token(),school);var spells=VIEWS.get(p.getUUID());
            int firebolt=spells.buttons().indexOf("translate:spell.irons_spellbooks.firebolt");h.assertTrue(firebolt>=0,"researched spell is selectable");
            Menus.click(p,spells.token(),firebolt);
            var spell=io.redspace.ironsspellbooks.api.registry.SpellRegistry.REGISTRY.get(ResourceLocation.parse("irons_spellbooks:firebolt"));
            h.assertTrue(io.redspace.ironsspellbooks.api.spells.ISpellContainer.getOrCreate(book).getIndexForSpell(spell)>=0,"typed screen action inscribes the real item component");npc.discard();
        }).thenSucceed();
    }
    @GameTest(template="test_empty",timeoutTicks=100)
    public static void copy_progress_and_no_free_actions(GameTestHelper h){
        var p=player(h,"OriginalTester");var copy=player(h,"CloneTester");
        Progress.data(p).putInt("exp_blackout",3);Progress.data(p).putInt("mastery_sword",51);Progress.copy(p,copy);
        h.assertTrue(Progress.data(copy).getInt("exp_blackout")==3,"death clone preserves expedition");
        h.assertTrue(Progress.data(copy).getInt("mastery_sword")==51,"death clone preserves mastery");
        Progress.data(copy).putInt("mastery_sword",0);
        h.assertTrue(Progress.data(p).getInt("mastery_sword")==51,"NBT is deep copied");
        Menus.click(p,"forged",0);h.assertTrue(Progress.data(p).getInt("exp_blackout")==3,"forged session cannot advance");h.succeed();
    }
}
