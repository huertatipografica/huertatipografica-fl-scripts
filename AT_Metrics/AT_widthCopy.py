#FLM: AT Copy widths to open fonts
# Copy the selected widths to other fonts
from robofab.world import CurrentFont,AllFonts,CurrentGlyph
fonts=AllFonts()
forigen=CurrentFont()
sel=forigen.selection

def copiaWidth(myWidth,gtarget):
	anchoFinal=gtarget.width
	anchoActual=myWidth
	anchoDif=anchoActual-anchoFinal
	anchoSide=anchoDif/2
	gtarget.leftMargin=gtarget.leftMargin+anchoSide
	gtarget.rightMargin=gtarget.rightMargin+anchoSide
	gtarget.width=myWidth
	print str(myWidth) + " > " + str(gtarget.width)

for f in fonts:
	for gname in sel:
		if gname in f:
			destino=f[gname]
			origen=forigen[gname]
			print f[gname]
			destino.mark=origen.mark
			copiaWidth(origen.width,destino)

			f.update()

print sel
print 'Done.'
