from flask import Blueprint, jsonify
maths = Blueprint('maths', __name__)
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