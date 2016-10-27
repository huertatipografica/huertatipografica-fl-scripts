#FLM: AT Rename from name,uni list

from robofab.world import CurrentFont,CurrentGlyph

f = CurrentFont()
g = CurrentGlyph()

myList = """Cdblstruck,0x2102
Ndblstruck,0x2115
Qdblstruck,0x211a
Rdblstruck,0x211d
eQee,0x2124
Ifraktur,0x2111
Rfraktur,0x211c
aleph,0x2135
arrowupdnbse,0x21a8
arrowdblleft,0x21d0
arrowdblright,0x21d2
arrowdblboth,0x21d4
universal,0x2200
existential,0x2203
emptyset,0x2205
gradient,0x2207
element,0x2208
suchthat,0x220b
ringoperator,0x2218
proportional,0x221d
orthogonal,0x221f
intersection,0x2229
measuredangle,0x2221
parallelto,0x2225
logicaland,0x2227
logicalor,0x2228
contourintegral,0x222e
asymptoticallyequalto,0x2243
estimates,0x2259
notlessthan,0x226e
notgreaterthan,0x226f
lessthanequivalentto,0x2272
greaterthanequivalentto,0x2273
uptack,0x22a5
verticalellipsis,0x22ee
plussigndotbelow,0x2a25
minussigndotbelow,0x2a2a
equalssigndotbelow,0x2a66"""

def hex2dec(s):
    #return hexadecimal string
    return int(s, 16)

def dec2hex(s):
	return hex(s)

def findUni(uni):
	uni = hex(uni)[2:]
	result = False
	for item in myList:
		uniVal=item[1][2:]
		if uni == uniVal:
			result = item
	return result

myList = myList.split("\n")
for i in range(len(myList)):
	myList[i]=myList[i].split(",")


for glyph in f:
	result = False
	if glyph.unicode:
		result = findUni(glyph.unicode)
	if result:
		glyph.name = result[0]
		glyph.mark = 20
		print glyph.name

f.update()
