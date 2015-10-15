#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys

if __name__ == "__main__":
    """
    Programa principal
    """
    fich = sys.argv[1]
    try:
        fichero = open(fich)
    except IndexError:
        print("Usage: python3 karaoke.py file.smil.")

    parser = make_parser()
    ssHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(ssHandler)
    parser.parse(fichero)

    tags = ssHandler.get_tags()
    print(tags)
