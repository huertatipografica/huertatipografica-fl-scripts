#FLM: AT Mark list of glyphs
from robofab.world import CurrentFont

f = CurrentFont()
myList = ['asciicircum','plus','minus','plusminus','equal','notequal','less','greater','lessequal','greaterequal','asciitilde','approxequal','multiply','numbersign','logicalnot','partialdiff','product','summation','radical','infinity','integral','lozenge','contourintegral','asymptoticallyequalto','estimates','notlessthan','notgreaterthan','lessthanequivalentto','greaterthanequivalentto','plussigndotbelow','minussigndotbelow','equalssigndotbelow','divide']

for g in myList:
	if f[g].selected:
		f[g].mark = 200
