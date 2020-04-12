from yamale import YamaleTestCase

import glob
from pathlib import Path

class TestSiteYaml(YamaleTestCase):
    base_dir = str(Path(__file__).resolve().parent.parent / 'out/group_vars')
    schema = 'ZZZZ-schema.yml'
    yaml = glob.glob(f'{base_dir}/????.yml')


    def runTest(self):
        self.assertTrue(self.validate())


