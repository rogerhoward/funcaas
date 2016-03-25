from flask import Blueprint, jsonify, render_template, abort, request
import os
name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
strings = Blueprint(name, __name__, template_folder='templates')
import config

# Format string
@strings.route('/format', methods=['POST'])
def formatter():
    """Formats a string using Python 3-style format()

    Args:
        string: the string to format
        formatter: an array of values to pass to the format() method

    Returns:
        result: JSON with result
    """
    if config.debug: print('formatter', request.method, request.args)

    try:
        payload = request.get_json()
        output_string = payload['string'].format(*payload['formatter'])
        return jsonify({'result': output_string})
    except:
        abort(500)


# Return module docs
@strings.route('/docs/{}'.format(name), methods=['GET'])
def docs():
    return render_template('{}.html'.format(name))