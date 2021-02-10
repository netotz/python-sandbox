'''
Creates a batch file for each ping to a certain IP adress so they can run at the same time.
Finally a main file that starts each ping is created. 
'''

import argparse
import os
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument(
    'ip',
    type=str,
    help='Base IP adress, e.g. 192.168.0.'
)
parser.add_argument(
    '-p', '--path',
    type=Path,
    default='',
    help='Path where the batch files will be created, defaults to current directory.'
)
args = parser.parse_args()
path = args.path
base_ip = args.ip

ids = (13, 31, 32, 34, 35, 36, 41, 42, 51, 52, 53)
filenames = []
for i in ids:
    ping_content = f'ping {base_ip}{i}\nexit 0'
    filename = f'ping{i}.bat'
    filenames.append(filename)
    filepath = os.path.join(path, filename)
    with open(filepath, 'w') as file:
        file.write(ping_content)

main_content = '\n'.join(f'start /min {f}' for f in filenames) + '\nexit 0'
filepath = os.path.join(path, 'run_all.bat')
with open(filepath, 'w') as file:
    file.write(main_content)
