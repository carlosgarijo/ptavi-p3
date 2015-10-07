#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

""" Creamos clase SmallSMILHandler """
class SmallSMILHandler(ContentHandler)
    """
    Clase para manejar SMIL
    """

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        #self.inrootlayout = 0
        self.width = ""
        self.height = ""
        self.bgcolor = ""
        #self.inregion = 0
        self.id = ""
        self.top = ""
        self.bottom = ""
        self.left = ""
        self.right = ""
        #self.inimg = 0
        self.src = ""
        self.region = ""
        self.begin = ""
        self.dur = ""
        #self.inaudio = 0
        #self.intextstream = 0

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == "root-layout":
            self.width = attrs.get('width',"")
            self.height = attrs.get('height',"")
            self.bgcolor = attrs.get('background-color',"")
        elif name == "region":
            self.id = attrs.get('id',"")
            self.top = attrs.get('top',"")
            self.bottom = attrs.get('bottom',"")
            self.left = attrs.get('left',"")
            self.right = attrs.get('right',"")
        elif name == "img":
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
        elif name == "audio":
            self.src = attrs.get('src',"")
            self.begin = attrs.get('begin',"")
            self.dur = attrs.get('dur',"")
        elif name == "textstream":
            self.src = attrs.get('src',"")
            self.region = attrs.get('region',"")


if __name__ == "__main__":
    """
    Programa principal
    """
    pass



