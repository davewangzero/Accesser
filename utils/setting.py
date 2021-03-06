import sys
from os import path
import json
import argparse

if hasattr(sys, '_MEIPASS'):
    basepath = sys._MEIPASS
else:
    basepath = '.'

with open(path.join(basepath, 'config.json.default'), 'r') as f:
    config = json.load(f)
if path.exists('config.json'):
    with open('config.json', 'r') as f:
        config = {**config, **json.load(f)}

parser = argparse.ArgumentParser()
parser.add_argument('--cli', action='store_true', help='do not open webui automatically')
args = parser.parse_args()
if args.cli:
    config['webui'] = False

def set(new):
    '''set value and return whether need to restart server'''
    global config
    if 'server' in new:
        restart_server = (new['server'] != config['server'])
    else:
        restart_server = False
    config = {**config, **new}
    return restart_server

def save():
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=2)
