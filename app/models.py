"""Application Models"""
from lxml import html


class PEP(object):
    def __init__(self, html_text):
        self.root = html.fromstring(html_text)
        nodes = self.root.xpath('//div[@id="content"]')
        if nodes:
            node = nodes[0]
            pieces = [piece for piece in node.itertext()]
        self.text = ''.join(pieces)
