"""
PEP Visualize
============= Web scrapping functions

"""
from flask import Flask, jsonify, abort, make_response, render_template
from app.models import PEP
import requests
import os
import re


app = Flask(__name__)

peps = []


@app.errorhandler(404)
def error_404(e):
    return jsonify({'errors': ('Resource Not Found', )}), 404


@app.errorhandler(400)
def error_400(e):
    return jsonify({'errors': ('Bad Request', )}), 400


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pep/<int:pep_number>')
def get_pep(pep_number):
    """Get the content div of the PEP by PEP number"""
    if not pep_number:
        return abort(400)

    if pep_number not in list(all_peps()):
        return abort(404)

    with open('pep_documents/pep-%04d.txt' % pep_number, 'rb') as f:
        text = f.read().decode('utf-8')
    pep = PEP(text)
    pep.parse_metadata()
    pep_dict = pep.to_dict()
    if pep_dict:
        return jsonify(dict(data=pep_dict, raw=text))
    else:
        return abort(404)


def all_peps():
    """Returns a generator of valid PEP numbers"""
    items = os.listdir('pep_documents')

    def is_pep(x):
        filename, ext = os.path.splitext(x)
        return 'pep-' in filename and '.txt' == ext.lower()

    peps = [pep for pep in items if is_pep(pep)]

    pattern = re.compile('^pep-(\d+)\.txt$')
    for pep in peps:
        match_obj = pattern.match(pep)
        if match_obj:
            yield int(match_obj.group(1))


@app.route('/pep')
def list_of_valid_pep_numbers():
    """Return a list of valid PEP numbers"""
    valid_numbers = list(all_peps())
    return jsonify(dict(data=valid_numbers))
