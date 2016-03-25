from flask import Blueprint, jsonify, render_template, abort, request
import os
name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
utilities = Blueprint(name, __name__, template_folder='templates')
import config

# Is the service alive?
@utilities.route('/is/alive')
def is_alive():
    """Returns yes if service is alive, otherwise returns no

    Returns:
        result: yes or no
    """
    if config.debug: print('is_alive', request.method, request.args)
    try:
        return jsonify({'result': 'yes'})
    except:
        return jsonify({'result': 'no'})


# Return True
@utilities.route('/return/true')
def return_true():
    """Returns True in Strict mode, or False for backwards compatibility.

    Returns:
        result: True or False, depending on ?mode
    """
    if config.debug: print('return_true', request.method, request.args)

    if request.args.get('mode') == 'strict':
        return jsonify({'result': True})
    else:
        return jsonify({'result': False})


# Is the service alive?
@utilities.route('/ping')
def ping():
    """Returns ping, but on error returns gnip

    Returns:
        result: ping or gnip
    """
    if config.debug: print('ping', request.method, request.args)
    try:
        return jsonify({'result': 'ping'})
    except:
        return jsonify({'result': 'gnip'})


# Return module docs
@utilities.route('/docs/{}'.format(name), methods=['GET'])
def docs():
    return render_template('{}.html'.format(name))