#FLM: AnchorLeft
# Version 1.0
# por Andres Torresi (http://www.huertatipografica.com.ar)
# Mueve anchor a la izquierda. Se recomienda asignar un atajo de teclado
from robofab.world import CurrentFont,CurrentGlyph
from robofab.interface.all.dialogs import AskString


def setAnchor(g,distancia,sentido,anchorName):
    anchorName2="_"+anchorName
    for a in g.anchors:
        if a.name == anchorName or a.name == anchorName2:
            if sentido=='y':
                a.y=(a.y)+distancia
            elif sentido=='x':
                a.x=(a.x)+distancia

def moveAnchor(distancia,sentido,anchorName):
    f = CurrentFont()
    if anchorName!='':
        for g in f:
            if g.selected:
                if len(g.anchors)>0:
                    setAnchor(g,distancia,sentido,anchorName)
                else:
                    print 'No hay anchors'

        f.update()
    else:
        print "Debe declarar un nombre de anchor primero."

try: anchorName
except NameError:
    print "Debe declarar el anchor"
else:
    moveAnchor(-5,'x',anchorName)


    