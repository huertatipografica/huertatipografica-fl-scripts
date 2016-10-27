#FLM: AT List component glyphs
from robofab.world import CurrentFont

font = CurrentFont()
output = ""

for gname in font.selection:
	g = font[gname]
	if len(g.components) >0 and len(g.contours)==0:
		output += g.name+","

print output
