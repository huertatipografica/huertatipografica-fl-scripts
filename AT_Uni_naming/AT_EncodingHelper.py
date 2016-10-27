#FLM: AT_EncodingHelper
from robofab.world import CurrentFont,CurrentGlyph

f = CurrentFont()
g = CurrentGlyph()

numStart=875

for gname in f.selection:
	glyph = f[gname]
	print glyph.name+" "+str(numStart)
	#print "glyph"+str(numStart)+" "+str(numStart)
	numStart+=1