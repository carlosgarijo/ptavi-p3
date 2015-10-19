#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json
import urllib


def init_parse(fichero):
    parser = make_parser()
    ssHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(ssHandler)
    parser.parse(fichero)
    tags = ssHandler.get_tags()
    return tags


def listado_ordenado(tags):
    listado = ""
    for subline in tags:
        listado = listado + subline[0]
        subdicc = subline[1]
        atribs = subdicc.items()
        for atrib, contenido in atribs:
            if contenido != "":
                listado = listado + "\t" + atrib + "=" + '"' + contenido + '"'
        listado = listado + "\n"
    print("Imprimiendo listado de etiquetas..." + "\n")
    return listado


def to_json(tags, fich_name=""):
    if not fich_name:
        fich_name = "local.json"
    else:
        fich_name = fich_name.replace(".smil", ".json")
    print("Convirtiendo a JSON... " + fich_name + "\n")
    with open(fich_name, 'w') as outfile_json:
        json.dump(tags, outfile_json, sort_keys=True,
                  indent=3, separators=(' ', ': '))


def url_local(tags):
    list_url = []
    for subline in tags:
        subdicc = subline[1]
        atribs = subdicc.items()
        for atrib, contenido in atribs:
            if atrib == "src":
                url = contenido
                list_url = url.split("/")
                remoto = list_url[0]
                if remoto == "http:":
                    arch_web = urllib.request.urlopen(url)
                    filename = list_url[-1]
                    print("Descargando... " + filename)
                    f = open(filename, "wb")
                    f.write(arch_web.read())
                else:
                    filename = contenido
                    print("Contenido ya en local... " + filename + "\n")

if __name__ == "__main__":
    fich = sys.argv[1]
    try:
        fichero = open(fich)
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    tags = init_parse(fichero)
    result = listado_ordenado(tags)
    print(result)
    to_json(tags, fichero.name)
    url_local(tags)
    to_json(tags)
    print(result)
