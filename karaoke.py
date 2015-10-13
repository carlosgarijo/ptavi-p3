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

    try:
        fich = open(sys.argv[1])
    except IndexError:
        print("Usage: python3 karaoke.py file.smil.")
