#FLM: AT MarkScheme v1.0

#GRUPOS
UC=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","ampersand"]
LC=["at","a","b","c","d","e","f","g","h","i","dotlessi","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","germandbls","ordfeminine","ordmasculine"]
Numbers=["zero","one","two","three","four","five","six","seven","eight","nine","zero.lf","one.lf","two.lf","three.lf","four.lf","five.lf","six.lf","seven.lf","eight.lf","nine.lf","zero.tf","one.tf","two.tf","three.tf","four.tf","five.tf","six.tf","seven.tf","eight.tf","nine.tf","zero.tosf","one.tosf","two.tosf","three.tosf","four.tosf","five.tosf","six.tosf","seven.tosf","eight.tosf","nine.tosf","one.smcp","two.smcp","three.smcp","four.smcp","five.smcp","six.smcp","seven.smcp","eight.smcp","nine.smcp","zero.smcp","twosuperior","threesuperior","onesuperior"]
DiacLetter=["Lslash","lslash","Scaron","Zcaron","scaron","zcaron","Agrave","Aacute","Acircumflex","Atilde","Adieresis","Aring","Ccedilla","Egrave","Eacute","Ecircumflex","Edieresis","Igrave","Iacute","Icircumflex","Idieresis","Ntilde","Ograve","Oacute","Ocircumflex","Otilde","Odieresis","Oslash","Ugrave","Uacute","Ucircumflex","Udieresis","Yacute","agrave","aacute","acircumflex","atilde","adieresis","aring","ccedilla","egrave","eacute","ecircumflex","edieresis","igrave","iacute","icircumflex","idieresis","ntilde","ograve","oacute","ocircumflex","otilde","odieresis","oslash","ugrave","uacute","ucircumflex","udieresis","yacute","Ydieresis","ydieresis"]
Diac=["grave","circumflex","tilde","dieresis","acute","cedilla","caron","ring","macron","breve","dotaccent","hungarumlaut","ogonek"]
Math=["minus","numbersign","percent","parenleft","parenright","asterisk","plus","less","equal","greater","bracketleft","backslash","bracketright","braceleft","bar","brokenbar","braceright","notequal","infinity","plusminus","lessequal","greaterequal","mu","partialdiff","summation","product","pi","integral","uni03A9","radical","approxequal","Delta","divide","lozenge","fraction","perthousand","onequarter","onehalf","threequarters","multiply","dagger","daggerdbl"]
Punt=["exclam","quotedbl","quotesingle","comma","hyphen","period","slash","colon","semicolon","question","underscore","questiondown","exclamdown","guillemotleft","guillemotright","ellipsis","endash","emdash","quotedblleft","quotedblright","quoteleft","quoteright","guilsinglleft","guilsinglright","quotesinglbase","quotedblbase","periodcentered"]
Bigram=["fi","fl","oe","ae","OE","AE"]
Currency=["dollar","Euro","cent","sterling","currency","yen","section"]

f=fl.font
glyphs = f.glyphs

for index in range(len(glyphs)):
    f[index].mark=0
    fl.UpdateGlyph(index)

def markGlyph(clase,color):
    for item in clase:
        if f.has_key(item):
            f[item].mark=color
            

#aplicar y pintar grupos
markGlyph(UC,1)
markGlyph(LC,1)
markGlyph(Numbers,25)
markGlyph(DiacLetter,10)
markGlyph(Diac,200)
markGlyph(Math,100)
markGlyph(Punt,125)
markGlyph(Bigram,150)
markGlyph(Currency,175)

fl.UpdateFont()


