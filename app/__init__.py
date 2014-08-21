"""
PEP Visualize
=============
Web scrapping functions

"""
from flask import Flask, jsonify, abort
from lxml import html
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

    root = html.fromstring(response.text)
    nodes = root.xpath('//div[@id="content"]')
    if nodes:
        node = nodes[0]
        pieces = [piece for piece in node.itertext()]
        return jsonify(dict(data=''.join(pieces)))
    else:
        return abort(404)
