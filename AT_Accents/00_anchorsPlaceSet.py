#FLM: 00. Place Anchors Set
# Version 1.0
# por Andres Torresi (http://www.huertatipografica.com.ar)
# Basado en el script de Ben Kiel
# No me hago responsable por problemas derivados del uso de este programa

# Este programa borra todos los anchors previamente configurados.
# Agrega los anchors en los glifos correspondientes. Para algunos de ellos preguntara la altura deseada.

#Estas listas se pueden editar o agregar listas personalizadas.
topListLC = [
"a",
"c",
"d",
"e",
"g",
"h",
"l",
"n",
"o",
"r",
"s",
"t",
"u",
"v",
"w",
"x",
"y",
"z",
"ae",
"oslash",
"dotlessi",
"dotlessj",
"ohorn",
"uhorn"
]

topListUC = [
"A",
"C",
"D",
"E",
"G",
"H",
"I",
"J",
"K",
"L",
"N",
"O",
"R",
"S",
"T",
"U",
"W",
"Y",
"Z",
"AE",
"Oslash",
"OE",
"Ohorn",
"Uhorn"
]

topListSC = [
"A.smcp",
"C.smcp",
"D.smcp",
"E.smcp",
"G.smcp",
"H.smcp",
"I.smcp",
"J.smcp",
"K.smcp",
"L.smcp",
"N.smcp",
"O.smcp",
"R.smcp",
"S.smcp",
"T.smcp",
"U.smcp",
"W.smcp",
"Y.smcp",
"Z.smcp",
"AE.smcp",
"Oslash.smcp",
"OE.smcp",
"Ohorn.smcp",
"Uhorn.smcp"
]

bottomList = [
"A",
"D",
"E",
"G",
"H",
"I",
"K",
"L",
"O",
"M",
"N",
"R",
"S",
"T",
"U",
"Y",
"Z",
"a",
"d",
"e",
"i",
"dotlessi",
"h",
"k",
"l",
"o",
"m",
"n",
"r",
"s",
"t",
"u",
"y",
"z",
"ohorn",
"uhorn",
"Ohorn",
"Uhorn",
"A.smcp",
"C.smcp",
"D.smcp",
"E.smcp",
"G.smcp",
"H.smcp",
"I.smcp",
"J.smcp",
"K.smcp",
"L.smcp",
"M.smcp",
"N.smcp",
"O.smcp",
"R.smcp",
"S.smcp",
"T.smcp",
"U.smcp",
"W.smcp",
"Y.smcp",
"Z.smcp",
"AE.smcp",
"Oslash.smcp",
"OE.smcp",
"Ohorn.smcp",
"Uhorn.smcp"
]


centerList = [
"L",
"L.smcp",
"l",
]

toprightList = [
"L",
"L.smcp",
"l",
"t",
]


_topList = [
"acute",
"grave",
"hungarumlaut",
"circumflex",
"caron",
"dotaccent",
"dieresis",
"dieresis.i",
'dieresisacute',
'dieresismacron',
"hookabove",
"ring",
"breve",
"macron",
"macron.i",
"tilde",
"tilde.i",
"tildecomb",
"ringacute",
"dieresisgrave",
"dieresiscaron",
"breveacute",
"brevegrave",
"brevehookabove",
"brevetilde",
"circumflexacute",
"circumflexgrave",
"circumflexhookabove",
"circumflextilde"
]

_bottomList = [
"commaaccent",
"dotbelowcomb",
"brevebelow",
"linebelow",
]

_centerList = [
"dotaccent",
"commaaccent"
]

_toprightList = [
"caron.alt",
]

ogonekList = [
"A",
"E",
"I",
"O",
"U",
"a",
"e",
"i",
"o",
"u"
]

_ogonekList = ["ogonek"]

cedillaList = ["C", "c", "S", "s", "t", "T", "C.smcp", "S.smcp", "T.smcp", ]
_cedillaList = ["cedilla"]


# Si hizo su propia lista agregela aqui
## Nombre de la lista, nombre del anchor, 1=Ingresar valor | 2=0, 'Nombre a mostrar'
accentGroups = [
[topListLC, 'top', 1, 'Lowercase'],
[topListUC, 'top', 1, 'Caps'],
[topListSC, 'top', 1, 'SmallCaps'],
[_topList, '_top', 1, 'Top accents'],
[bottomList, 'bottom', 0, 'Bottom'],
[_bottomList, '_bottom', 0, 'Bottom accents'],
[centerList, 'center', 1, 'Right'],
[_centerList, '_center', 1, 'Right accents'],
[ogonekList, 'ogonek', 0, 'Ogonek'],
[_ogonekList, '_ogonek', 0, 'Ogonek accent'],
[cedillaList, 'cedilla', 0, 'Cedilla'],
[_cedillaList, '_cedilla', 0, 'Cedilla accent'],
[_toprightList, '_topright', 0, 'Top right'],
[toprightList, 'topright', 0, 'Top right']
]


###########
from robofab.interface.all.dialogs import AskString
from robofab.interface.all.dialogs import Message
from robofab.interface.all.dialogs import SearchList
from robofab.world import CurrentFont

#asks for a number. if allowZeroOrLess is 0 it will not allow a number that is zero or less
def getNumber(message, allowZeroOrLess):
    userInput = AskString(message)
    if userInput is not None:
        try:
            int(userInput)
        except ValueError:
            userInput = getNumber('Please enter a number', allowZeroOrLess)
        if (userInput <= 0) and (allowZeroOrLess == 0):
            userInput = getNumber('Please enter a number greater than 0', 0)
        return int(userInput)

def getGlyphWidth(glyph):
    box = glyph.box
    width = box[2] - box[0]
    return width

def checkAnchors(g, name):
    for a in g.anchors:
        if a.name==name:
            return 1

#Program
font = CurrentFont()

for g in font:
    if g.selected:
        g.clearAnchors()

for group in accentGroups:
    name = group[1]
    groupName = group[3]
    if group[2] == 1:
        y = getNumber('Vertical Position for ' + name + ' in ' + groupName, 1)
    else:
        y = group[2]
    for glyph in group[0]:
		print glyph
		if '.smcp' in glyph:
			glyph = glyph.lower()
		if font.has_key(glyph) and font[glyph].selected:
			x = int(getGlyphWidth(font[glyph]) / 2) + font[glyph].leftMargin
			font[glyph].mark = 100
			if checkAnchors(font[glyph],name)!=1:
				font[glyph].appendAnchor(name, (x, y))
#        else:
#            newGlyph = font[glyph]
#            newGlyph.autoUnicodes()
#            newGlyph.update()




font.update()
Message('All done!')
	
