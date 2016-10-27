#FLM: AT Copy mark color
# Copia el color de marca de los glifos seleccionados
from robofab.world import CurrentFont,AllFonts,CurrentGlyph
fonts=AllFonts()
forigen=CurrentFont()
sel=forigen.selection

output = ''
for f in fonts:
	for gname in sel:
		if gname in f:
			destino=f[gname]
			origen=forigen[gname]
			output+=gname+"\n"
			destino.mark=origen.mark

	f.update()

print output
print sel
print 'Done.'
