#FLM: AT Compatibility check
#Check compatibility of selected glyphs between the current font and declared fontCompare (Postcrit Full Name)
# By Andres Torresi
# http://www.huertatipografica.com

#fullName of font you want to compare with current font
fontCompare='ABBvoice Bold';

colorCompatible=150
colorIncompatible=255

#--------FUNCIONES------------------

def chequear(g,f2,f1):
    f1name=f1.info.postscriptFullName
    f2name=f2.info.postscriptFullName
    if f1.has_key(g.name):
		compatible=f1[g.name].isCompatible(f2[g.name], True)
		if compatible[0]==False:
			print "No es compatible el glifo "+g.name+" en "+f1name
			print compatible
			g.mark=colorIncompatible
			f1[g.name].mark=colorIncompatible
    else:
        print "No existe el glifo "+g.name+" en "+f1name


###########

from robofab.world import AllFonts,CurrentFont,CurrentGlyph
from robofab.interface.all.dialogs import Message, ProgressBar

fonts=AllFonts()

for f in fonts:
    if f.info.postscriptFullName==fontCompare:
		f1=f

f2=CurrentFont()
glyph=CurrentGlyph()
fl.SetUndo()
error=0
print f1,f2


if len(fonts)<2:
    error="Debe abrir dos fuentes para comparar"
elif f1.path==f2.path:
    error="Origen y destino son la misma fuente."

if error==0:
    tickCount = len(f2.selection)
    bar = ProgressBar('Chequeando...', tickCount)
    tick = 0

    for g in f2.keys():
        if f2[g].selected or g.index == fl.iglyph or g == glyph.name:
            chequear(f2[g],f2,f1)
            bar.tick(tick)
            tick = tick+1
    bar.close()
    f1.update()
    f2.update()
else:
    print error
