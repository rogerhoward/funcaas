"""Application configuration file.

Load by 'import config', not 'from config import *'
Access properties as 'config.property'
"""

import os, json

project_directory = os.path.dirname(os.path.realpath(__file__))
modules_dir = 'modules'

log = True
debug = True
host = '0.0.0.0'
port = 5000
