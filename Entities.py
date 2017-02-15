# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:30:03 2015

@author: ade
"""


def createObj(item):
    return {"LINE": Line}.get(item[0][1], Entities)(*item)


class Entities(object):
    gcodes_common = [-1, 0, 5, 102, 330, 360, 100, 67, 410, 8, 6, 62, 48, 60, 92, 310]
    codedict = {}

    def __init__(self, *codelist):
        self.codedict = {}
        for key, val in codelist:
            self.codedict[key] = val
        self.setDefaults()

    def setDefaults(self):
        if '67' not in self.codedict:
            self.codedict['67'] = 0
        if '6' not in self.codedict:
            self.codedict['6'] = 'BYLAYER'
        if '62' not in self.codedict:
            self.codedict['62'] = 'BYLAYER'
        if '48' not in self.codedict:
            self.codedict['48'] = '1.0'
        if '60' not in self.codedict:
            self.codedict['60'] = '0'

    def __str__(self):
        out = ''
        for key, val in self.codedict.items():
            out += str(key) + ' : ' + val + '\n'
        return out


class Line(Entities):
    startpoint = ()
    endpoint = ()
    name = 'LINE'
    gcodes = [100, 39, 10, 20, 30, 11, 21, 31, 210, 220, 230]

    def __init__(self, *codelist):
        super(Line, self).__init__(*codelist)
        if self.codedict == {}: pass
        codes = self.gcodes + self.gcodes_common
        for key in self.codedict.keys():
            if int(key) not in codes:
                raise ValueError('%s group code not accepted' % key)
        self.startpoint = (self.codedict['10'], self.codedict['20'], self.codedict['30'])
        self.endpoint = (self.codedict['11'], self.codedict['21'], self.codedict['31'])

    def __str__(self):
        return str(self.startpoint) + str(self.endpoint)


if __name__ == '__main__':
    print("Entities as main")

    a = Entities()
    #b = Line()
