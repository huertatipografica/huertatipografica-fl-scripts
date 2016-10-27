#FLM: AT Asignar PUA
from robofab.world import CurrentFont, CurrentGlyph
f = CurrentFont()
 
# alternatively, create a glyph object for the current glyph
newUnicode=57344
for g in f:
	if g.unicodes==[]:
		g.unicodes=[newUnicode+1]
		newUnicode=newUnicode+1
		print str(g.unicodes)+" | "+g.name
f.update()

