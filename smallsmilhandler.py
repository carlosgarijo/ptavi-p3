#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys


""" Creamos clase SmallSMILHandler """


class SmallSMILHandler(ContentHandler):
    """
    Clase para manejar SMIL
    """

    def __init__(self):
        """
        Constructor. Inicializamos las variables
        """
        self.width = ""
        self.height = ""
        self.bgcolor = ""
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        self.tag = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == "root-layout":
            self.width = attrs.get('width', "")
            self.height = attrs.get('height', "")
            self.bgcolor = attrs.get('background-color', "")
            self.tag = (self.tag + ["root-layout", "width", self.width,
                        "heigth", self.height, "background-color",
                        self.bgcolor])
        elif name == "region":
            self.id = attrs.get('id', "")
            self.top = attrs.get('top', "")
            self.bottom = attrs.get('bottom', "")
            self.left = attrs.get('left', "")
            self.right = attrs.get('right', "")
            self.tag = (self.tag + ["region", "id", self.id, "top",
                        self.top, "bottom", self.bottom, "left", self.left,
                        "right", self.right])
        elif name == "img":
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.tag = (self.tag + ["img", "src", self.src, "region",
                        self.region, "begin", self.begin, "dur", self.dur])
        elif name == "audio":
            self.src = attrs.get('src', "")
            self.begin = attrs.get('begin', "")
            self.dur = attrs.get('dur', "")
            self.tag = (self.tag + ["audio", "src", self.src, "begin",
                        self.begin, "dur", self.dur])
        elif name == "textstream":
            self.src = attrs.get('src', "")
            self.region = attrs.get('region', "")
            self.tag = (self.tag + ["textstream", "src", self.src,
                        "region", self.region])

    def get_tags(self):
        print(self.tag)


if __name__ == "__main__":
    """
    Programa principal
    """
    fichero = sys.argv[1]
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open(fichero))
    print(cHandler.get_tags())
