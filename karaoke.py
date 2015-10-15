#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys


def listado_ordenado(tags):
    listado = ""
    for diccs in tags:
        atrib_line = ""
        for key in diccs.keys():
            if key != "name" and diccs[key] != "":
                atrib_line = atrib_line + key + "=" + diccs[key] + "\t"
        listado = listado + diccs["name"] + "\t" + atrib_line + "\n"
    return listado

if __name__ == "__main__":

    fich = sys.argv[1]
    try:
        fichero = open(fich)
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    parser = make_parser()
    ssHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(ssHandler)
    parser.parse(fichero)

    tags = ssHandler.get_tags()
    result = listado_ordenado(tags)
    print(result)
