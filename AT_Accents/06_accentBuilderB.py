#FLM: 06. Accent Builder Beta
# Version 1.0
# por Andres Torresi (http://www.huertatipografica.com.ar)

#Utiliza la lista de glifos y componentes en robofab/trunk/Lib/robofab/tools/glyphConstruction.py
#genera los glifos de la lista



theList = [
"Aacute",
"Acircumflex",
"Adieresis",
"Agrave",
"Atilde",
"Amacron",
"Abreve",
"Cacute",
"AEacute",
"Ccircumflex",
"Cdotaccent",
"Ccaron",
"Ccedilla",
"Dcaron",
"Eacute",
"Edieresis",
"Egrave",
"Ecircumflex",
"Emacron",
"Ebreve",
"Edotaccent",
"Ecaron",
"Hcircumflex",
"hcircumflex",
"Gcircumflex",
"Gbreve",
"Gdotaccent",
"uni0122",
"Iacute",
"Icircumflex",
"Igrave",
"Idieresis",
"Itilde",
"Imacron",
"Ibreve",
"Idotaccent",
"Jcircumflex",
"uni0136",
"Lacute",
"uni013B",
"Ntilde",
"Nacute",
"uni0145",
"Ncaron",
"Ograve",
"Otilde",
"Oacute",
"Ocircumflex",
"Odieresis",
"Omacron",
"Obreve",
"Ohungarumlaut",
"Racute",
"uni0156",
"Rcaron",
"Sacute",
"Scircumflex",
"Scedilla",
"Scaron",
"uni0162",
"Tcaron",
"Uacute",
"Udieresis",
"Ugrave",
"Ucircumflex",
"Utilde",
"Umacron",
"Ubreve",
"Uring",
"Uhungarumlaut",
"Wcircumflex",
"Wgrave",
"Wacute",
"Wdieresis",
"Yacute",
"Ycircumflex",
"Ydieresis",
"Ygrave",
"Zacute",
"Zdotaccent",
"Zcaron",
"aacute",
"acircumflex",
"adieresis",
"agrave",
"atilde",
"amacron",
"abreve",
"aeacute",
"cacute",
"ccircumflex",
"cdotaccent",
"ccaron",
"ccedilla",
"eacute",
"edieresis",
"egrave",
"ecircumflex",
"emacron",
"ebreve",
"edotaccent",
"ecaron",
"gcircumflex",
"gbreve",
"gdotaccent",
"uni0123",
"iacute",
"icircumflex",
"itilde",
"imacron",
"ibreve",
"igrave",
"idieresis",
"jcircumflex",
"uni0137",
"lacute",
"uni013C",
"ntilde",
"nacute",
"uni0146",
"ncaron",
"oacute",
"ocircumflex",
"odieresis",
"ograve",
"otilde",
"omacron",
"obreve",
"ohungarumlaut",
"uacute",
"udieresis",
"ugrave",
"ucircumflex",
"utilde",
"umacron",
"ubreve",
"uring",
"uhungarumlaut",
"racute",
"uni0157",
"rcaron",
"tcaron",
"sacute",
"scircumflex",
"scedilla",
"scaron",
"uni0163",
"wcircumflex",
"wgrave",
"wacute",
"wdieresis",
"yacute",
"ydieresis",
"ycircumflex",
"ygrave",
"zacute",
"zdotaccent",
"zcaron",
"dcaron",
"lcaron",
"Ldot",
"ldot",
"napostrophe",
"Lcaron",
"Oslashacute",
"oslashacute",
"gcommaaccent",
"kcommaaccent",
"lcommaaccent",
"ncommaaccent",
"rcommaaccent",
"scommaaccent",
"tcommaaccent",
"Gcommaaccent",
"Kcommaaccent",
"Lcommaaccent",
"Ncommaaccent",
"Rcommaaccent",
"Scommaaccent",
"Tcommaaccent",
]

from robofab.world import CurrentFont
from robofab.tools.toolsAll import readGlyphConstructions

f = CurrentFont()

import string

con = readGlyphConstructions()
theList.sort()

def accentify(f, preflight=False):
    print 'start accentification', f.info.fullName
    slots = con.keys()
    slots.sort()
    for k in theList:
        build=''
        if k[-3:] in [".sc"]:
            isSpecial = True
            tag = k[-3:]
            name = k[:-3]
        else:
            isSpecial = False
            tag = ""
            name = k
        parts = con.get(name, None)
        if parts is None:
            print k, "no definido en glyphConstruction.py ?"
            continue

        base = parts[0]
        accents = parts[1:]
        if f.has_key(base):
            for a in f[base].anchors:
                if a.name==parts[1][1]:
                    build='ok'
                    break
            if build=='ok':
                #print k
                f.generateGlyph(k, preflight=preflight)
                f[k].mark = 100
                f[k].autoUnicodes()
                f[k].update()
                build=''
            else:
                print base+" no tiene asignado el anchor "+parts[1][1]
                f[base].mark=250
        else:
            print "No existe el glifo "+base
    f.update()

accentify(f)
print 'Listo'
 