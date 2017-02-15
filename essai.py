# -*- coding: utf-8 -*-
"""
Created on 23 nov. 2015

@author: ade
"""

from Entities import *


class Dxf:
    section = {'HEADER': [],
               'CLASSES': [],
               'TABLES': [],
               'BLOCKS': [],
               'ENTITIES': [],
               'OBJECTS': [],
               'THUMBNAILIMAGE': []
               }

    def __init__(self, dxffile):

        if dxffile == '': pass
        self.readfile(dxffile)
        self.entlist = self.readsection(*self.section['ENTITIES'])
        self.entity = []
        for item in self.entlist:
            self.entity.append(createObj(item))

    def readcode(self, f):
        """
        Reads two lines in dxf file, outputs (groupcode, value)
        """
        code = f.readline().strip('\n').strip()
        value = f.readline().strip('\n').strip()
        return code, value

    def readfile(self, dxffile):
        with open(dxffile, 'r') as f:
            out = self.readcode(f)
            while out[1] != 'EOF':
                if out == ('0', 'SECTION'):
                    out = self.readcode(f)
                    sect = out[1]
                    print
                    sect
                    out = self.readcode(f)
                    while out[1] != "ENDSEC":
                        self.section[sect] += [out]
                        out = self.readcode(f)
                else:
                    out = self.readcode(f)

    def readsection(self, *seclist):
        itemlist = []
        returnlist = []
        for item in seclist:
            if item[0] == '0':
                if itemlist != []:
                    returnlist.append(itemlist)
                itemlist = [item]
            else:
                itemlist.append(item)
        returnlist.append(itemlist)
        return returnlist


class Section:
    None
    """
    def __init__(self, *codelist):
        l = []
        for codes in codelist:
            if codes[0] == '0':
                if l != []: self.entlist.append(l)
                l = [codes]
            else: 
                l.append(codes)
    """


class Header(Section):
    None


class Classes(Section):
    None


class Tables(Section):
    None


class Blocks(Section):
    None


class Objects(Section):
    None


class Thumbnailimage(Section):
    None


a = Dxf('Gear Sample-iss4.DXF')
