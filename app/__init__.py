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
    url = 'http://www.python.org/dev/peps/pep-%04d' % pep_number
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify(dict(errors=['Something wrong'])), 400

    pep = PEP(response.text)
    if pep.text:
        return jsonify(dict(data=pep.text))
    else:
        return abort(404)
