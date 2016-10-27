#FLM: AT Mitre selected points
"""Mitre Glyph:

mitreSize : Length of the segment created by the mitre. The default is 4.
maxAngle :  Maximum angle in radians at which nodes will be mitred. The default is .9 (about 50 degrees).
            Works for both inside and outside angles

"""

mitresize=2
angle=.9

import math

def getContourRange(nid,g):
	cID = g.FindContour(nid)
	cStart = g.GetContourBegin(cID)
	cEnd = cStart + g.GetContourLength(cID) - 1
	return cStart,cEnd

def getNextNode(nid,g):
	cStart,cEnd = getContourRange(nid,g)
	if nid == cEnd:
		return g[cStart]
	else:
		return g[nid + 1]

def getPrevNode(nid,g):
	cStart,cEnd = getContourRange(nid,g)
	if nid == cStart:
		return g[cEnd]
	else:
		return g[nid - 1]

def normalizeVector(p):
	m = getMagnitude(p);
	if m != 0:
		return p*(1/m)
	else:
		return Point(0,0)

def getMagnitude(p):
	return math.sqrt(p.x*p.x + p.y*p.y)

def getDistance(v1,v2):
	return getMagnitude(Point(v1.x - v2.x, v1.y - v2.y))

def getAngle(v1,v2):
	angle = math.atan2(v1.y,v1.x) - math.atan2(v2.y,v2.x)
	return (angle + (2*math.pi)) % (2*math.pi)

def getNodeVectors(g,nid):
	n = g[nid]
	p = Point(n.x, n.y)
	nn = getNextNode(nid, g)
	pn = getPrevNode(nid, g)

	nVect = Point(-p.x + nn.x, -p.y + nn.y)
	pVect = Point(-p.x + pn.x, -p.y + pn.y)

	if nn.type == nCURVE:
		nn = Point(nn[1].x,nn[1].y)
	else:
		nn = Point(nn.x,nn.y)

	if n.type == nCURVE:
		pn = Point(n[2].x,n[2].y)
	else:
		pn = Point(pn.x,pn.y)

	nVect = Point(-p.x + nn.x, -p.y + nn.y)
	pVect = Point(-p.x + pn.x, -p.y + pn.y)
	return pVect,nVect


def mitreCorner(g, nid, mitreSize = 5., maxAngle = .9):

	pVect,nVect = getNodeVectors(g,nid)

	# dont mitre if segment is too short
	if abs(getMagnitude(pVect)) < mitreSize * 2 or abs(getMagnitude(nVect)) < mitreSize * 2:
		return

	angle = getAngle(nVect,pVect)
	nVect = normalizeVector(nVect)
	pVect = normalizeVector(pVect)

	# only mitre corners sharper than maxAngle
#	if angle > maxAngle and angle < math.pi * 2 - maxAngle:
#		return

	radius = mitreSize / abs(getDistance(nVect,pVect))

	offset1 = Point(round(pVect.x * radius), round(pVect.y * radius))
	offset2 = Point(round(nVect.x * radius), round(nVect.y * radius))

	g.Insert(Node(nLINE, Point(g.nodes[nid].x, g.nodes[nid].y)), nid+1)

	n1 = g.nodes[nid]
	n2 = g.nodes[nid + 1]

	n1[0].x += offset1.x
	n1[0].y += offset1.y
	n2[0].x += offset2.x
	n2[0].y += offset2.y

	return True

def mitreGlyph(g,mitreSize,maxAngle):
	fl.SetUndo()
	i = 0
	while i < len(g.nodes):
		n = g[i]
                if n.selected:
                    if mitreCorner(g,i,mitreSize,maxAngle):
                            i+=1
		i += 1
	fl.UpdateGlyph()


#default 4, .9
mitreGlyph(fl.glyph,mitresize,angle)
