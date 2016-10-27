#FLM: 07. Declare your anchor
# Version 1.0
# por Andres Torresi (http://www.huertatipografica.com.ar)


#Declara un nombre de anchor para ser utilizado en otros scripts.
#El script marca todos los glifos que tienen un anchor 'nombre' o '_nombre'
#y los almacena en las variables anchorName y anchorName2 para su uso posterior


### dialogo
from robofab.world import CurrentFont
class MyDialog:
  def __init__(self):
    self.d = Dialog(self)
    self.d.size = Point(250, 150)
    self.d.Center()
    self.d.AddControl(STATICCONTROL, Rect(aIDENT, aIDENT, aIDENT, aIDENT), "frame", STYLE_FRAME)
    self.d.AddControl(STATICCONTROL, Rect(aIDENT2, aIDENT2, aAUTO, aAUTO), "label1", STYLE_LABEL, "Nombre anchor:")
    self.d.AddControl(EDITCONTROL, Rect(20, aNEXT, aIDENT2, aAUTO), "anchorNameUser", STYLE_EDIT, "")
    self.anchorNameUser = ""

  def on_anchorNameUser(self, code):
    self.d.GetValue("anchorNameUser")
  def on_ok(self, code):
    return 1
  def Run(self):
    return self.d.Run()

d = MyDialog()

if d.Run()!= 1:
    error="si"
else:
    error="no"

anchorName=d.anchorNameUser
anchorName2 = "_"+anchorName

f=CurrentFont()
for g in f:
	anchor=0
	if len(g.anchors)>0:
		for a in g.anchors:
			if a.name==anchorName or a.name==anchorName2:
				anchor=1
		if anchor==1:
			g.mark=200
		else:
			g.mark=0
		

f.update()


