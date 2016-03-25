#!/usr/bin/env python

"""Server run file.

Run by './server.py'
Access properties as 'config.property'
"""

import pkgutil, sys
from flask import Flask, Blueprint
import config
app = Flask(__name__)


modules = pkgutil.iter_modules(path=[config.modules_dir])
for loader, mod_name, ispkg in modules: 
    if mod_name not in sys.modules:
        loaded_mod = __import__(config.modules_dir+"."+mod_name, fromlist=[mod_name])
        for obj in vars(loaded_mod).values():
            if isinstance(obj, Blueprint):
                app.register_blueprint(obj)


app.run(debug=config.debug, host=config.host, port=config.port)
