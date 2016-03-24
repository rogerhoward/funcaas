#!/usr/bin/env python

import json, os, sys
import config
from flask import Flask, Response, send_file, jsonify, abort, request

app = Flask(__name__)


# Deploy project
@app.route('/is/int/<value>', methods=['GET'])
def is_int(value):
    """Receives value and returns if it looks and smells
       like an int

    Args:
        value: the value to test for int-ness

    Returns:
        bool: JSON with True or False
    """

    try:
        value_as_int = int(value)
        return jsonify({'response':True})
    except:
        return jsonify({'response':False})


if __name__ == '__main__':
    app.run(debug=config.debug, host='0.0.0.0', port=5000)