from pathlib import Path
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
import install_pack

class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        base=Path(self.temp.name);self.src=base/'release';self.dst=base/'instance';self.dst.mkdir()
        for name,text in {'world/level.dat':'template','world/datapacks/test/pack.mcmeta':'{}','kubejs/server_scripts/fantasia_exam_runtime.js':'new','config/ftbquests/quests/data.snbt':'new quests'}.items():
            p=self.src/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
        p=self.dst/'kubejs/server_scripts/fantasia_exam_runtime.js';p.parent.mkdir(parents=True);p.write_text('old')
        (p.parent/'unrelated.js').write_text('preserve')
    def tearDown(self):self.temp.cleanup()
    def test_backup_and_unrelated_files_and_legacy_jar(self):
        mods=self.dst/'mods';mods.mkdir()
        with zipfile.ZipFile(mods/'old.jar','w') as z:z.writestr('META-INF/neoforge.mods.toml','[[mods]]\nmodId="fantasia_core"')
        result=install_pack.install(self.dst,source=self.src)
        backup=Path(result['backup'])
        self.assertEqual((backup/'kubejs/server_scripts/fantasia_exam_runtime.js').read_text(),'old')
        self.assertEqual((self.dst/'kubejs/server_scripts/unrelated.js').read_text(),'preserve')
        self.assertTrue((backup/'mods/old.jar').exists());self.assertFalse((mods/'old.jar').exists())
        self.assertEqual((Path(result['world'])/'level.dat').read_text(),'template')
    def test_existing_world_refused_before_changes(self):
        world=self.dst/'saves/Fantasia_Campaign_RC1';world.mkdir(parents=True);(world/'level.dat').write_text('valuable')
        with self.assertRaises(FileExistsError):install_pack.install(self.dst,source=self.src)
        self.assertEqual((world/'level.dat').read_text(),'valuable')
        self.assertEqual((self.dst/'kubejs/server_scripts/fantasia_exam_runtime.js').read_text(),'old')
    def test_dry_run_and_traversal(self):
        install_pack.install(self.dst,source=self.src,dry_run=True)
        self.assertFalse((self.dst/'fantasia_backups').exists())
        with self.assertRaises(ValueError):install_pack.install(self.dst,world_name='../escape',source=self.src)
    def test_failed_copy_rolls_back_old_files(self):
        original=install_pack.shutil.copy2
        def broken(src,dst,*args,**kw):
            if str(src).endswith('fantasia_exam_runtime.js'):raise OSError('simulated disk failure')
            return original(src,dst,*args,**kw)
        with patch.object(install_pack.shutil,'copy2',broken):
            with self.assertRaises(OSError):install_pack.install(self.dst,source=self.src)
        self.assertEqual((self.dst/'kubejs/server_scripts/fantasia_exam_runtime.js').read_text(),'old')
        self.assertFalse((self.dst/'saves/Fantasia_Campaign_RC1').exists())

if __name__=='__main__':unittest.main(verbosity=2)
