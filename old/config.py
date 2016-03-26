"""Application configuration file.

Load by 'import config', not 'from config import *'
Access properties as 'config.property'
"""

import os, json

log = True
debug = True
host = '0.0.0.0'
port = 5000

project_directory = os.path.dirname(os.path.realpath(__file__))

modules_directory_name = 'modules'
modules_directory = os.path.join(project_directory, modules_directory_name)

loaded_modules = []
modules_blacklist = ['home']
for child in os.listdir(modules_directory):
    if os.path.isdir(os.path.join(modules_directory, child)) and child not in modules_blacklist:
        loaded_modules.append(child)