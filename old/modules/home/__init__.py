from flask import Blueprint, jsonify, render_template, abort, request
import os
name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
home = Blueprint(name, __name__, template_folder='templates')
import config



# Static Routes
@home.route('/')
def root():
    print 'home'
    print config.loaded_modules
    return render_template('home.html', modules= config.loaded_modules)


@home.route('/<path:path>')
def static_proxy(path):
    return home.send_static_file(path)