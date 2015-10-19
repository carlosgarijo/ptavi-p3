#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import smallsmilhandler
import sys
import json
import urllib


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):
    def __init__(self, fichero):
        parser = make_parser()
        ssHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(ssHandler)
        parser.parse(fichero)
        self.tags = ssHandler.get_tags()

    def __str__(self):
        listado = ""
        for subline in self.tags:
            listado = listado + subline[0]
            subdicc = subline[1]
            atribs = subdicc.items()
            for atrib, contenido in atribs:
                if contenido != "":
                    listado = (listado + "\t" + atrib +
                               "=" + '"' + contenido + '"')
            listado = listado + "\n"
        return listado

    def to_json(self, fich_name=""):
        if not fich_name:
            fich_name = "local.json"
        else:
            fich_name = fich_name.replace(".smil", ".json")
        with open(fich_name, 'w') as outfile_json:
            json.dump(self.tags, outfile_json, sort_keys=True,
                      indent=3, separators=(' ', ': '))

    def do_local(self):
        for subline in self.tags:
            atribs = subline[1]
            for key in atribs:
                if atribs[key].startswith('http://'):
                    url = atribs[key]
                    filename = url.split('/')[-1]
                    urllib.request.urlretrieve(url, filename)
                    atribs[key] = filename

if __name__ == "__main__":

    fich = sys.argv[1]
    try:
        fichero = open(fich)
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    Karaoke = KaraokeLocal(fichero)
    print(Karaoke)
    Karaoke.to_json(fichero.name)
    Karaoke.do_local()
    Karaoke.to_json()
    print(Karaoke)
