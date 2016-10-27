#FLM: AT Sufijo & Generar v2
#por Andres Torresi


### dialogo
class MyDialog:
  def __init__(self):
    self.d = Dialog(self)
    self.d.size = Point(250, 150)
    self.d.Center()
    self.d.title = "Ingresa el sufijo (Ej: alt)"
    self.d.AddControl(STATICCONTROL, Rect(aIDENT, aIDENT, aIDENT, aIDENT), "frame", STYLE_FRAME)
    self.d.AddControl(STATICCONTROL, Rect(aIDENT2, aIDENT2, aAUTO, aAUTO), "label1", STYLE_LABEL, "")
    self.d.AddControl(EDITCONTROL, Rect(100, aNEXT, aIDENT2, aAUTO), "suffix", STYLE_EDIT, "Sufijo:")
    self.d.AddControl(CHECKBOXCONTROL, Rect(100,aNEXT,aIDENT2,aIDENT), 'generar', STYLE_CHECKBOX, ' '+'Generar glifos?')
    self.generar =""
    self.suffix = ""

  def on_suffix(self, code):
    self.d.GetValue("suffix")
    self.d.GetValue("generar")
  def on_ok(self, code):
    return 1
  def Run(self):
    return self.d.Run()

d = MyDialog()

if d.Run()!= 1:
    error="si"
else:
    error="no"

suffix=d.suffix
generar=d.generar

###

def replaceGlyphClass(f,find,replace):
        classes_old = f.classes
        classes_new = f.classes
        for index in range(len(classes_new)):
            classes_new[index]=classes_new[index].replace(' '+find,' '+replace,1)
        f.classes = classes_new
        fl.UpdateFont()


def checkName(glyphs,name):
    for index in range(len(glyphs)):
        if glyphs[index].name == name:
            print 'Ya existe el glifo '+glyphs[index].name
            match='true'
            break
        else:
            match='false'
    return match

def createGlyph(f,g,name):
    newGlyph = f.GenerateGlyph(name)
    f.glyphs.append(newGlyph)
    fl.UpdateFont(fl.ifont)
    f[name].mark=100

def process(f,g,suffix,generar):
    newName=''
    if suffix!='':
        name= g.name
        part=name.split('.')
        partlen=len(part)
        if partlen>1:
            suffix='.'+suffix
            part[partlen-1]=suffix
            
            for p in range(partlen):
                newName=newName+part[p]
            check=checkName(f.glyphs,newName)
            if check!='true':
                fl.SetUndo(index)
                g.name=newName
                g.mark=100
                replaceGlyphClass(f,name,newName)
        else:
            if generar=='0':
                print 'El glifo '+g.name+' no tiene sufijo para renombrar.'
            else:
                newName=name+'.'+suffix
                check=checkName(f.glyphs,newName)
                if check!='true':
                    createGlyph(f,g,newName)



if error!='si':
    font = fl.font
    glyphs = font.glyphs

    for index in range(len(glyphs)):
      if fl.Selected(index) and index != fl.iglyph :
        process(font,glyphs[index], suffix,generar)
        fl.UpdateGlyph(index)

    process(font,glyphs[fl.iglyph], suffix,generar)
    fl.UpdateGlyph()
    
