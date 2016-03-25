from flask import Blueprint, jsonify
utilities = Blueprint('utilities', __name__)
import config

# Is the service alive?
@utilities.route('/is/alive')
def is_alive():
    """Returns yes if service is alive, otherwise returns no

    Returns:
        result: yes or no
    """
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
    try:
        return jsonify({'result': 'ping'})
    except:
        return jsonify({'result': 'gnip'})