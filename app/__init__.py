"""
PEP Visualize
=============
Web scrapping functions

"""
from flask import Flask, jsonify, abort
from app.models import PEP
import requests


app = Flask(__name__)


@app.route('/pep/<int:pep_number>')
def get_pep(pep_number):
    """
    Get the content div of the PEP by PEP number
    """
    if not pep_number:
        return jsonify(dict(errors=['PEP Number is missing'])), 400
    with open('pep_documents/pep-%04d.txt' % pep_number, 'rb') as f:
        text = f.read().decode('utf-8')
    pep = PEP(text)
    pep.parse_metadata()
    if pep.title:
        return jsonify(dict(data=pep.title))
    else:
        return abort(404)
