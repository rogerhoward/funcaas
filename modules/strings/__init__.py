from flask import Blueprint, jsonify
strings = Blueprint('strings', __name__)
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
    try:
        payload = request.get_json()
        output_string = payload['string'].format(*payload['formatter'])
        return jsonify({'result': output_string})
    except:
        abort(500)