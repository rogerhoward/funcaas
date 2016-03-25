#!/usr/bin/env python

"""Server run file.

Run by './server.py'
Access properties as 'config.property'
"""

import pkgutil, sys
from flask import Flask, Blueprint
import config
app = Flask(__name__)

MODULES_DIR = 'modules'
modules = pkgutil.iter_modules(path=[MODULES_DIR])
for loader, mod_name, ispkg in modules: 
    if mod_name not in sys.modules:
        loaded_mod = __import__(MODULES_DIR+"."+mod_name, fromlist=[mod_name])
        for obj in vars(loaded_mod).values():
            if isinstance(obj, Blueprint):
                app.register_blueprint(obj)


app.run(debug=config.debug, host='0.0.0.0', port=5000)
