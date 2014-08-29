"""
PEP Visualize
=============
Web scrapping functions

"""
from flask import Flask, jsonify, abort, make_response
from app.models import PEP
import requests


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
        return jsonify(dict(data=pep_dict))
    else:
        return abort(404)
