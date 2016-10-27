#FLM: 02. Copy anchors from other vfb.
# Version 1.0
# Ingrese el nombre (PS Full Name) de la fuente origen de la cual desea copiar los anchors
# Copiara solo a los glifos seleccionados
forigen='Labelia-RegularUFO';


from robofab.world import CurrentFont,AllFonts,CurrentGlyph
from robofab.interface.all.dialogs import Message, ProgressBar

def copiaAnchors(forigen,fdestino,gname,tick):
	actualAnchors=[]
	print fdestino["A"]
	print forigen["A"]
	if forigen[gname]:
		if len(forigen[gname].anchors)>0:
			for a in fdestino[gname].anchors:
				actualAnchors.append(a.name)
			for a in forigen[gname].anchors:
				if  a.name in actualAnchors:
					print gname+" ya tiene anchor "+a.name
				else:
					fdestino[gname].appendAnchor(a.name, (a.x,a.y))
					print "Anchor "+a.name+' copiado a'+gname
					fdestino[gname].mark=180
	bar.tick(tick)
	tick = tick+1

fonts=AllFonts()

for f in fonts:
	if f.info.postscriptFullName==forigen:
		forigen=f

fcurrent=CurrentFont()
glyph=CurrentGlyph()
fl.SetUndo()

tickCount = len(fcurrent.selection)
bar = ProgressBar('Copiando anchors...', tickCount)
tick = 0

for gname in fcurrent.selection:
	copiaAnchors(forigen,fcurrent,gname,tick)

bar.close()
Message('Anchors copiados.')
fdestino.update()