"""
PEP Visualize
============= Web scrapping functions

"""
from flask import Flask, jsonify, abort, make_response
from app.models import PEP
import requests
import os
import re


app = Flask(__name__)


@app.errorhandler(404)
def error_404(e):
    return jsonify({'errors': ('Resource Not Found', )}), 404


@app.errorhandler(400)
def error_400(e):
    return jsonify({'errors': ('Bad Request', )}), 400


@app.route('/pep/<int:pep_number>')
def get_pep(pep_number):
    """Get the content div of the PEP by PEP number"""
    if not pep_number:
        return abort(400)

    with open('pep_documents/pep-%04d.txt' % pep_number, 'rb') as f:
        text = f.read().decode('utf-8')
    pep = PEP(text)
    pep.parse_metadata()
    pep_dict = pep.to_dict()
    if pep_dict:
        return jsonify(dict(data=pep_dict, raw=text))
    else:
        return abort(404)


@app.route('/pep')
def list_of_valid_pep_numbers():
    """Return a list of valid PEP numbers"""
    items = os.listdir('pep_documents')

    def is_pep(x):
        filename, ext = os.path.splitext(x)
        return 'pep-' in filename and '.txt' == ext.lower()

    peps = [pep for pep in items if is_pep(pep)]

    valid_numbers = []
    pattern = re.compile('^pep-(\d+)\.txt$')
    for pep in peps:
        match_obj = pattern.match(pep)
        if match_obj:
            valid_numbers.append(int(match_obj.group(1)))

    return jsonify(dict(data=valid_numbers))
