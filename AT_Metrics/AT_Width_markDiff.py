#FLM: AT Mark different widths
# Marca en la fuente actual los glifos con distinto ancho que la referencia
from robofab.world import CurrentFont,AllFonts,CurrentGlyph
fonts=AllFonts()
forigen='Cambria';
for f in fonts:
	if f.info.postscriptFullName==forigen:
		forigen=f

fcurrent=CurrentFont()
g=CurrentGlyph()
fl.SetUndo()
def copiaWidth(forigen,fdestino):
	g=CurrentGlyph()
	for glyph in fdestino:
		if glyph.selected:
			g=glyph.name
			anchoFinal=fdestino[g].width
			anchoActual=forigen[g].width
			anchoDif=anchoActual-anchoFinal
			if anchoFinal!=anchoActual:
				fdestino[g].mark=100
				fdestino[g].update()
				fdestino.update()
				print str(g)
				print str(forigen[g].width) + " > " + str(fdestino[g].width)

copiaWidth(forigen,fcurrent)
