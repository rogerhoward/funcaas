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
        int(value)
        return jsonify({'response':True})
    except:
        return jsonify({'response':False})


# Deploy project
@app.route('/format', methods=['POST'])
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


# Is the service alive?
@app.route('/alive', methods=['GET'])
def alive():
    """Returns yes if service is alive, otherwise returns no

    Returns:
        result: yes or no
    """
    try:
        return jsonify({'result': 'yes'})
    except:
        return jsonify({'result': 'no'})


# Static Routes
@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/<path:path>')
def static_proxy(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(debug=config.debug, host='0.0.0.0', port=5000)