#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.diccs = {'root-layout': ['width', 'height', 'background-color'],
                      'region': ['id', 'top', 'bottom', 'left', 'right'],
                      'img': ['src', 'region', 'begin', 'dur'],
                      'audio': ['src', 'begin', 'dur'],
                      'textstream': ['src', 'region']}

        self.tag = []

    def startElement(self, name, attrs):

        if name in self.diccs:
            help_dicc = {}
            for atributo in self.diccs[name]:
                help_dicc[atributo] = attrs.get(atributo, "")
            self.tag.append([name, help_dicc])

    def get_tags(self):
        return self.tag


if __name__ == "__main__":
    fichero = sys.argv[1]
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(fichero))
    print(cHandler.get_tags())
