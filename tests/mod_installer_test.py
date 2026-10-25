import importlib.util
from pathlib import Path
import tempfile,unittest,zipfile
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('install_mod',ROOT/'tools/install_mod.py');installer=importlib.util.module_from_spec(spec);spec.loader.exec_module(installer)
def jar(path,mod):
 path.parent.mkdir(parents=True,exist_ok=True)
 with zipfile.ZipFile(path,'w') as z:z.writestr('META-INF/neoforge.mods.toml',f'[[mods]]\nmodId="{mod}"\nversion="1.0.0"\n')
 return path
class InstallerTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name);self.instance=self.root/'instance';self.instance.mkdir();self.jar=jar(self.root/'release/fantasia-campaign.jar','fantasia_campaign')
 def tearDown(self):self.temp.cleanup()
 def legacy(self):
  for name in ('fantasia_exam_runtime.js','fantasia_campaign_runtime.js','fantasia_magic_runtime.js'):
   p=self.instance/'kubejs/server_scripts'/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('legacy')
  world=self.instance/'saves/Campaign';(world/'datapacks/fantasia_campaign').mkdir(parents=True);(world/'datapacks/fantasia_campaign/pack.mcmeta').write_text('legacy pack')
  (world/'region').mkdir();(world/'region/r.0.0.mca').write_bytes(b'keep region');(world/'level.dat').write_bytes(b'keep world')
  jar(self.instance/'mods/old-custom-core.jar','fantasia_core');jar(self.instance/'mods/unrelated.jar','another_mod')
  return world
 def test_migration_backs_up_only_conflicting_content(self):
  world=self.legacy();installer.install(self.instance,self.jar)
  self.assertEqual((world/'region/r.0.0.mca').read_bytes(),b'keep region');self.assertEqual((world/'level.dat').read_bytes(),b'keep world')
  self.assertTrue((self.instance/'mods/unrelated.jar').exists());self.assertTrue((self.instance/'mods'/self.jar.name).exists());self.assertFalse((world/'datapacks/fantasia_campaign').exists())
  self.assertEqual(len(list((self.instance/'fantasia-backups').rglob('fantasia_exam_runtime.js'))),1)
 def test_dry_run_changes_nothing(self):
  self.legacy();before={str(p.relative_to(self.instance)):p.read_bytes() for p in self.instance.rglob('*') if p.is_file()}
  installer.install(self.instance,self.jar,True);after={str(p.relative_to(self.instance)):p.read_bytes() for p in self.instance.rglob('*') if p.is_file()};self.assertEqual(before,after)
 def test_failed_copy_restores_every_legacy_file(self):
  world=self.legacy();original_write=Path.write_bytes
  def failing(path,data):
   if path.suffix=='.installing':raise OSError('disk full')
   return original_write(path,data)
  with patch.object(Path,'write_bytes',failing):
   with self.assertRaises(OSError):installer.install(self.instance,self.jar)
  self.assertTrue((world/'datapacks/fantasia_campaign/pack.mcmeta').exists());self.assertTrue((self.instance/'mods/old-custom-core.jar').exists());self.assertTrue((self.instance/'kubejs/server_scripts/fantasia_exam_runtime.js').exists())
 def test_mods_symlink_escape_is_rejected(self):
  outside=self.root/'outside';outside.mkdir();(self.instance/'mods').symlink_to(outside,target_is_directory=True)
  with self.assertRaises(ValueError):installer.install(self.instance,self.jar)
  self.assertEqual(list(outside.iterdir()),[])
 def test_can_reinstall_from_existing_mod_path(self):
  current=jar(self.instance/'mods/fantasia-campaign.jar','fantasia_campaign');content=current.read_bytes();installer.install(self.instance,current)
  self.assertEqual(current.read_bytes(),content)
if __name__=='__main__':unittest.main()
