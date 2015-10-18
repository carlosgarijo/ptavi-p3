#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json
import urllib


def listado_ordenado(tags):
    listado = ""
    for diccs in tags:
        atrib_line = ""
        for key in diccs.keys():
            if key != "name" and diccs[key] != "":
                atrib_line = atrib_line + key + "=" + diccs[key] + "\t"
        listado = listado + diccs["name"] + "\t" + atrib_line + "\n"
    return listado

def to_json(fichero):
    json_listado = json.dumps(fichero)
    #print(json_listado)
    with open('/home/garijos/Escritorio/PTAVI/ptavi-p3/karaoke.json', 'w') as outfile:
        json.dump(json_listado, outfile)

def url_local(tags):
    list_url = []
    for diccs in tags:
        for key in diccs.keys():
            if key == "src":
                url = diccs[key]
                list_url = url.split("/")
                remoto = list_url[0]
                if remoto == "http:":
                    arch_web = urllib.request.urlopen(url)
                    filename = list_url[-1]
                    print(filename)
                    f = open(filename, "wb")
                    f.write(arch_web.read())
                else:
                    filename = diccs[key]
                    print(filename)

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

    #to_json(fichero)
    url_local(tags)
