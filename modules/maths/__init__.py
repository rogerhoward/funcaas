from flask import Blueprint, jsonify, render_template
import os
name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
maths = Blueprint(name, __name__, template_folder='templates')
import config


# Is value an int?
@maths.route('/is/int/<value>', methods=['GET'])
def is_int(value):
    """Receives value and returns if it looks and smells
       like an int

    Args:
        value: the value to test for int-ness

    Returns:
        bool: JSON with True or False
    """
    if config.debug: print('is_int {}'.format(__name__))
    try:
        int(value)
        return jsonify({'response':True})
    except:
        return jsonify({'response':False})


# Is the service alive?
@maths.route('/ping')
def ping():
    """Returns ping, but on error returns gnip

    Returns:
        result: ping or gnip
    """
    try:
        return jsonify({'result': 'ping'})
    except:
        return jsonify({'result': 'gnip'})


# Return module docs
@maths.route('/docs/{}'.format(name), methods=['GET'])
def docs():
    return render_template('{}.html'.format(name))