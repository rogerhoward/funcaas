"""Application configuration file.

Load by 'import config', not 'from config import *'
Access properties as 'config.property'
"""

import os, json

project_directory = os.path.dirname(os.path.realpath(__file__))

log = True
debug = True