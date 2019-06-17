import configparser
from subprocess import run
from sys import argv, exit

try: 
    len(argv) != 1
except:
    exit(0)

masterpubkey = argv[1]

config = configparser.ConfigParser()

config.read('config.ini')

config['master-public-keys']['one'] =  str(masterpubkey)

with open('config.ini', 'w') as configfile:
    config.write(configfile)

run(['electrum-personal-server', 'config.ini'])
