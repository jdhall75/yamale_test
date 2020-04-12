import random
import string
from pathlib import Path
import yaml

from faker import Faker

num_files = 4

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))

def generate_random_int(length):
    return int(''.join(random.choice(string.digits) for _ in range(length)))

def init_dir(path):
    file_path = Path(path)
    if file_path.exists():
        return file_path

    file_path.mkdir(
            mode=0o0755,
            parents=True,
            exist_ok=True)

    return file_path


for _ in range(num_files):
    file_name = generate_random_string(4)
    fake = Faker()

    out_path = init_dir('./out/group_vars')
    out_file = out_path / file_name
    
    content = {
            'site_abvr': file_name,
            'site_addr': fake.address(),
            'hub_number': generate_random_int(2)
            }

    yaml_contents = yaml.dump(content)
    out_file.write_text(yaml_contents)


