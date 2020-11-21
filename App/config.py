import json, os


environment = os.environ.get('ENV')
if environment is None:
    environment = 'staging'

CONFIG = None

with open('environment.'+environment+'.json') as config_file:
    CONFIG = json.load(config_file)
    CONFIG['ENV']=environment