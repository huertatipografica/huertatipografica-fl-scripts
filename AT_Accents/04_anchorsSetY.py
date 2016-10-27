#FLM: 04. Set anchor Y
#FLM: 01. Place Anchor
# Version 1.0
# por Andres Torresi (http://www.huertatipografica.com.ar)
# No me hago responsable por problemas derivados del uso de este programa

#Establece la altura vertical de los anchors previamente declarados

from robofab.world import CurrentFont

class MyDialog:
  def __init__(self):
    self.d = Dialog(self)
    self.d.size = Point(180, 120)
    self.d.Center()
    self.d.AddControl(STATICCONTROL, Rect(aIDENT, aIDENT, aIDENT, aIDENT), "frame", STYLE_FRAME)
    self.d.AddControl(STATICCONTROL, Rect(aIDENT2, aIDENT2, aAUTO, aAUTO), "label1", STYLE_LABEL, "Altura anchor "+anchorName)
    self.d.AddControl(EDITCONTROL, Rect(20, aNEXT, aIDENT3, aAUTO), "anchorY", STYLE_EDIT, "")
    self.anchorY = ""

  def on_anchorY(self, code):
    self.d.GetValue("anchorY")
  def on_ok(self, code):
    return 1
  def Run(self):
    return self.d.Run()

def setAnchor(g,anchorY):
    for a in g.anchors:
        if a.name==anchorName or a.name == anchorName2:
            a.y=anchorY

try: anchorName
except NameError:
    print "Debe declarar el anchor antes de ejecutar este script."
else:
    d = MyDialog()
    if d.Run()!= 1:
        error="si"
    else:
        anchorY=int(d.anchorY)
        f = CurrentFont()

        for g in f.selection:
            if f[g].anchors>0:
                setAnchor(f[g],anchorY)
        f.update()



