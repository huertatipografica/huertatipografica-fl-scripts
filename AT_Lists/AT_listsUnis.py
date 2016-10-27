#FLM: AT List of unicodes table
from robofab.world import CurrentFont

mathList=["notequal",
"lessequal",
"greaterequal",
"approxequal",
"micro",
"minute",
"second",
"partialdiff",
"product",
"summation",
"divisionslash",
"bulletoperator",
"radical",
"infinity",
"integral",
"lozenge",
"increment",
"ohm",
"florin",
"commercialminus",
"numero",
"careof",
"pi",
"Cdblstruck",
"Ndblstruck",
"Qdblstruck",
"Rdblstruck",
"Zdblstruct ",
"Ifraktur",
"Rfraktur",
"aleph",
"arrowupdnbse",
"arrowdblleft",
"arrowdblright",
"arrowdblboth",
"universal",
"existential",
"emptyset",
"gradient",
"element",
"suchthat",
"ringoperator",
"proportional",
"orthogonal",
"intersection",
"measuredangle",
"parallelto",
"logicaland",
"logicalor",
"contourintegral",
"asymptoticallyequalto",
"estimates",
"notlessthan",
"notgreaterthan",
"lessthanequivalentto",
"greaterthanequivalentto",
"uptack",
"verticalellipsis",
"plussigndotbelow",
"minussigndotbelow",
"equalssigndotbelow"]

font = CurrentFont()
output = ""

for gname in font.selection:
	if gname not in mathList:
		font[gname].mark=25
		uni=hex(font[gname].unicode)
		uni = uni[:2] + uni[2:].rjust(4, "0").upper()
		print gname,uni
