#FLM: AT Notes delete
from robofab.world import CurrentFont

font = CurrentFont()
output = ""

for gname in font.selection:
	g = font[gname]
	g.note = ""

print output
