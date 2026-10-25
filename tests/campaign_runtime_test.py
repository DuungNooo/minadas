"""Execute shipped mcfunction logic in a bounded model, not a Minecraft server."""
from pathlib import Path
import unittest
from support.mcfunction_model import World, Context

ROOT = Path(__file__).resolve().parents[1]
DIM = 'fantasia:campaign'
NPC = {'mine':(160,65,-14),'canal':(0,65,146),'forest':(-160,65,-14),
       'storm':(0,65,-174),'defense':(-160,65,146),'archive':(160,65,146),
       'north':(-160,65,-174),'east':(160,65,-174),'south':(320,65,-14),
       'castle':(320,65,140),'tutorial':(6,65,0)}


class CampaignTests(unittest.TestCase):
    def setUp(self):
        self.w = World(ROOT/'world/datapacks')
        self.w.setscore('#ready','fa_world',1)
        self.p = self.w.player()
        self.w.function('fantasia:npc/spawn',context=Context(dimension=DIM))
        self.w.function('fantasia:join',self.p)

    def act(self, value, pos=None, player=None):
        p=player or self.p
        if pos is not None:p.pos=pos
        p.scores['fa_action']=value
        self.w.function('fantasia:action',p)

    def second(self):
        self.w.function('fantasia:second')

    def eliminate_wave(self, encounter, player=None):
        p=player or self.p
        mobs=[m for m in self.w.entities if m.alive and 'fa_enemy_'+encounter in m.tags]
        self.assertTrue(mobs, f'{encounter} must actually spawn enemies')
        for mob in mobs:
            mob.alive=False
            self.w.function(f'fantasia:encounter/{encounter}/kill',p)
        self.second()

    def enter(self, travel_id):
        # Physical walking between nearby stations is represented by position changes.
        self.act(1, self.p.pos)
        self.assertEqual(self.p.pos,(0,65,-8))
        self.act(travel_id,(0,65,0))

    def station(self, name, pos):
        self.p.pos=pos
        self.w.function('fantasia:station/'+name,self.p)

    def introduction(self):
        self.p.advancements.add('fantasia_research:exam/complete')
        self.act(11,NPC['tutorial'])
        self.act(12,NPC['tutorial'])
        self.assertIn('fa_in_tutorial',self.p.tags)
        self.eliminate_wave('tutorial')
        self.assertEqual(self.p.scores['fa_stage'],1)

    def test_full_playthrough_all_four_endings_are_reachable_once(self):
        self.introduction()
        for region,travel,action,steps in [
            ('mine',101,20,[]),
            ('canal',102,21,[('canal_east',(8,65,160)),('canal_west',(-8,65,160)),('canal_center',(0,65,155))]),
            ('forest',103,22,[('forest_west',(-168,65,0)),('forest_center',(-160,65,-5)),('forest_east',(-152,65,0))]),
            ('storm',104,23,[('storm_west',(-8,65,-160)),('storm_east',(8,65,-160)),('storm_center',(0,65,-165))])]:
            self.p.pos=(0,65,0) if region=='mine' else self.p.pos
            if region=='mine': self.act(travel,(0,65,0))
            else: self.p.pos=NPC[previous];self.enter(travel)
            for step,pos in steps:self.station(step,pos)
            self.act(action,NPC[region]);self.eliminate_wave(region)
            if region=='mine':
                self.station('miner',(152,65,0));self.station('fire_core',(168,65,0))
            self.assertEqual(self.p.scores['fa_'+region],5)
            previous=region
        self.second();self.assertEqual(self.p.scores['fa_stage'],2)
        self.p.pos=NPC['storm'];self.enter(105)
        self.act(30,NPC['defense'])
        for _ in range(3):self.eliminate_wave('defense')
        self.assertEqual(self.p.scores['fa_stage'],3)
        self.p.pos=NPC['defense'];self.enter(106)
        for side,pos in [('west',(152,65,160)),('east',(168,65,160)),('center',(160,65,155))]:
            self.station('archive_'+side,pos)
        self.act(31,NPC['archive']);self.assertEqual(self.p.scores['fa_stage'],4)
        previous='archive'
        for region,travel,action in [('north',107,40),('east',108,41),('south',109,42)]:
            self.p.pos=NPC[previous];self.enter(travel);self.act(action,NPC[region]);self.eliminate_wave(region)
            self.assertEqual(self.p.scores['fa_'+region],5);previous=region
        self.second();self.assertEqual(self.p.scores['fa_stage'],5)
        for school in ['fire','ice','nature','lightning','ender','holy','blood','void','evocation']:
            for tier in [1,2,3]:self.assertIn(f'fantasia_research:{school}_tier_{tier}',self.p.advancements)
        self.p.pos=NPC['south'];self.enter(110)
        self.act(50,NPC['castle'])
        self.assertIn('fa_in_castle',self.p.tags,'entrance outside arena radius must still enroll initiator')
        self.eliminate_wave('castle')
        self.assertEqual(self.w.score('#wave_castle','fa_world'),2)
        self.station('seal_west',(310,65,175));self.station('seal_east',(330,65,175))
        self.assertEqual(self.w.score('#wave_castle','fa_world'),3)
        self.eliminate_wave('castle');self.assertEqual(self.p.scores['fa_stage'],6)
        for ending in range(1,5):
            # Four independent save-state choices at the same final checkpoint.
            self.p.scores['fa_stage']=6
            self.act(60+ending,NPC['castle'])
            self.assertEqual(self.p.scores['fa_ending'],ending)
            self.assertEqual(self.p.scores['fa_stage'],7)
            self.act(60+(ending%4+1),NPC['castle'])
            self.assertEqual(self.p.scores['fa_ending'],ending)

    def test_exam_gear_distance_and_dimension_gate(self):
        self.act(12,NPC['tutorial']);self.assertNotIn('fa_fighting',self.p.tags)
        self.act(11,(500,65,500));self.assertEqual(self.p.scores['fa_gear'],0)
        self.p.dimension='minecraft:overworld';self.act(11,NPC['tutorial'])
        self.assertEqual(self.p.scores['fa_gear'],0)
        self.p.dimension=DIM;self.act(11,NPC['tutorial'])
        sword_count=self.p.inventory['minecraft:iron_sword']
        self.act(11,NPC['tutorial']);self.assertEqual(self.p.inventory['minecraft:iron_sword'],sword_count)
        self.act(12,NPC['tutorial']);self.assertNotIn('fa_fighting',self.p.tags)
        self.act(110,(0,65,0));self.assertEqual(self.p.pos,(0,65,0))
        self.act(61,NPC['castle']);self.assertEqual(self.p.scores['fa_stage'],0)

    def test_bad_puzzle_order_remote_interaction_and_timeout(self):
        self.introduction()
        self.station('canal_west',(-8,65,160));self.assertEqual(self.p.scores['fa_canal'],0)
        self.station('canal_east',(999,65,999));self.assertEqual(self.p.scores['fa_canal'],0)
        self.station('storm_west',(-8,65,-160));self.assertEqual(self.p.scores['fa_storm'],1)
        for _ in range(20):self.second()
        self.assertEqual(self.p.scores['fa_storm'],0)
        self.station('storm_east',(8,65,-160));self.assertEqual(self.p.scores['fa_storm'],0)

    def test_party_enrollment_kill_credit_and_death(self):
        self.introduction()
        peer=self.w.player('Peer',NPC['mine']);peer.scores.update(self.p.scores)
        distant=self.w.player('Distant',(0,65,0));distant.scores.update(self.p.scores)
        self.act(20,NPC['mine'])
        self.assertIn('fa_in_mine',self.p.tags);self.assertIn('fa_in_mine',peer.tags)
        self.assertNotIn('fa_in_mine',distant.tags)
        self.w.function('fantasia:encounter/mine/kill',distant)
        self.assertEqual(self.w.score('#kills_mine','fa_world'),0)
        self.p.scores['fa_deaths']+=1;self.second()
        self.assertNotIn('fa_in_mine',self.p.tags);self.assertEqual(self.p.pos,(0,65,-8))
        self.eliminate_wave('mine',peer)
        self.assertEqual(peer.scores['fa_mine'],1)
        self.assertEqual(self.p.scores['fa_mine'],0)
        self.assertEqual(distant.scores['fa_mine'],0)

    def test_leave_abort_reentry_and_reset_are_personal(self):
        self.introduction();self.act(20,NPC['mine'])
        self.p.pos=(1000,65,1000);self.second()
        self.assertEqual(self.w.score('#mine','fa_world'),0)
        self.assertNotIn('fa_fighting',self.p.tags)
        self.act(20,NPC['mine']);self.assertIn('fa_fighting',self.p.tags)
        self.w.function('fantasia:recover',self.p)
        self.second();self.assertEqual(self.w.score('#mine','fa_world'),0)
        self.assertEqual(self.p.scores['fa_stage'],1)
        self.w.function('fantasia:admin/reset_player',self.p)
        self.assertEqual(self.p.scores['fa_stage'],0)
        self.assertNotIn('fantasia_research:campaign/intro',self.p.advancements)

    def test_join_repeat_does_not_reset_progress(self):
        self.introduction();inventory=self.p.inventory.copy()
        self.w.function('fantasia:join',self.p)
        self.assertEqual(self.p.scores['fa_stage'],1)
        self.assertEqual(self.p.inventory,inventory)


if __name__=='__main__':unittest.main(verbosity=2)
