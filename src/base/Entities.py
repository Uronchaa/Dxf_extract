# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 09:30:03 2015

@author: ade

types of ENTITIES described at http://www.autodesk.com/techpubs/autocad/acadr14/dxf/entities_section_al_u05_c.htm
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


class Face3D(Entities):
    # TODO = implement data retrieval for 3DFACE entities
    pass


class Solid3D(Entities):
    # TODO = implement data retrieval for 3DSOLID entities
    pass


class Solid3D(Entities):
    # TODO = implement data retrieval for 3DSOLID entities
    pass


class ACAD_PROXY_ENTITY(Entities):
    # TODO = implement data retrieval for ACAD_PROXY_ENTITY entities
    pass


class ARC(Entities):
    # TODO = implement data retrieval for ARC entities
    pass


class ATTDEF(Entities):
    # TODO = implement data retrieval for ATTDEF entities
    pass


class ATTRIB(Entities):
    # TODO = implement data retrieval for ATTRIB entities
    pass


class BODY(Entities):
    # TODO = implement data retrieval for BODY entities
    pass


class CIRCLE(Entities):
    # TODO = implement data retrieval for CIRCLE entities
    pass


class DIMENSION(Entities):
    # TODO = implement data retrieval for DIMENSION entities
    # Common Dimension Group Codes
    # Aligned, Linear, and Rotated Dimension Group Codes
    # Linear and Rotated Dimension Group Codes
    # Radial and Diameter Dimension Group Codes
    # Angular Dimension Group Codes
    # Ordinate Dimension Group Codes
    # Dimension Style Overrides
    pass


class ELLIPSE(Entities):
    # TODO = implement data retrieval for ELLIPSE entities
    pass


class HATCH(Entities):
    # TODO = implement data retrieval for HATCH entities
    Boundary
    Path
    Data
    Pattern
    Data
    pass


class IMAGE(Entities):
    # TODO = implement data retrieval for IMAGE entities
    pass


class INSERT(Entities):
    # TODO = implement data retrieval for INSERT entities
    pass


class LEADER(Entities):
    # TODO = implement data retrieval for LEADER entities
    pass


class LWPOLYLINE(Entities):
    # TODO = implement data retrieval for LWPOLYLINE entities
    pass


class MLINE(Entities):
    # TODO = implement data retrieval for MLINE entities
    pass


class MTEXT(Entities):
    # TODO = implement data retrieval for MTEXT entities
    pass


class OLEFRAME(Entities):
    # TODO = implement data retrieval for OLEFRAME entities
    pass


class OLE2FRAME(Entities):
    # TODO = implement data retrieval for OLE2FRAME entities
    pass


class POINT(Entities):
    # TODO = implement data retrieval for POINT entities

    pass


class POLYLINE(Entities):
    # TODO = implement data retrieval for POLYLINE entities
    # Polyface Meshes
    pass


class RAY(Entities):
    # TODO = implement data retrieval for RAY entities
    pass


class REGION(Entities):
    # TODO = implement data retrieval for REGION entities
    pass


class SEQEND(Entities):
    # TODO = implement data retrieval for SEQEND entities
    pass


class SHAPE(Entities):
    # TODO = implement data retrieval for SHAPE entities
    pass


class SOLID(Entities):
    # TODO = implement data retrieval for SOLID entities
    pass


class SPLINE(Entities):
    # TODO = implement data retrieval for SPLINE entities
    pass


class TEXT(Entities):
    # TODO = implement data retrieval for TEXT entities
    pass


class TOLERANCE(Entities):
    # TODO = implement data retrieval for TOLERANCE entities
    pass


class TRACE(Entities):
    # TODO = implement data retrieval for TRACE entities
    pass


class VERTEX(Entities):
    # TODO = implement data retrieval for VERTEX entities
    pass


class VIEWPORT(Entities):
    # TODO = implement data retrieval for VIEWPORT entities
    pass


class XLINE(Entities):
    # TODO = implement data retrieval for XLINE entities
    pass

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
    # b = Line()
