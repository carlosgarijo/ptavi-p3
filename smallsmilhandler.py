#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.root_layout = ['width', 'height', 'background-color']
        self.region = ['id', 'top', 'bottom', 'left', 'right']
        self.img = ['src', 'region', 'begin', 'dur']
        self.audio = ['src', 'begin', 'dur']
        self.textstream = ['src', 'region']
        self.tag = []

    def startElement(self, name, attrs):

        if name == 'root-layout':
            dicc = {"name": "Root-Layout"}
            for atributo in self.root_layout:
                dicc[atributo] = attrs.get(atributo, "")
            self.tag.append(dicc)

        elif name == 'region':
            dicc = {"name": "Region"}
            for atributo in self.region:
                dicc[atributo] = attrs.get(atributo, "")
            self.tag.append(dicc)

        elif name == 'img':
            dicc = {"name": "Img"}
            for atributo in self.img:
                dicc[atributo] = attrs.get(atributo, "")
            self.tag.append(dicc)

        elif name == 'audio':
            dicc = {"name": "Audio"}
            for atributo in self.audio:
                dicc[atributo] = attrs.get(atributo, "")
            self.tag.append(dicc)

        elif name == 'textstream':
            dicc = {"name": "Textstream"}
            for atributo in self.textstream:
                dicc[atributo] = attrs.get(atributo, "")
            self.tag.append(dicc)

    def get_tags(self):
        return self.tag


if __name__ == "__main__":
    fichero = sys.argv[1]
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(fichero))
    print(cHandler.get_tags())
