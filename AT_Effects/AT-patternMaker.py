#FLM: AT PatternMaker

###########################
#INSTRUCTIONS 
# Create glyphs with patterns to apply to the font. Be sure the glyphs have the same 
# sufix, point and consecutive 3 digit numbers starting from 001.
# Example: sufix.001, sufix.002, sufix.003, etc.

# Execute the script and enter the sufix for the glyphs that will work as patterns. 
# Example:
# glyphs:pattern.001,pattern.002,pattern.003...
# the sufix will be «pattern»
# Please be sure the numbers after suffix are of 3 digits and consecutive

# The script will substract all your patterns from the selected characters contour, alternating randomly between all your patterns.

###########################

#INSTRUCCIONES
# Cree glifos con patrones para aplicar a la fuente. Asegúrese que los glifos tienen el mismo sufijo 
# seguido de un punto y 3 números que serán consecutivos en cada patrón, empezando por 001.
# Ejemplo: sufijo.001, sufijo.002, sufijo.003, etc.

# Ejecute el script e ingrese el sufijo de sus glifos patrones
# Ejemplo
# glifos: marca.001,marca.002,marca.003
# el sufijo será «marca»
# Asegúrese que los números de los patrones son consecutivos, empezando desde 001.

# El script sustraerá sus patrones del contorno de los caracteres seleccionados, alternando de forma aleatoria entre cada uno.

###########################

class MyDialog:
  def __init__(self):
    self.d = Dialog(self)
    self.d.size = Point(400, 100)
    self.d.Center()
    self.d.title = "Enter pattern glyphs suffix name"
    self.d.AddControl(STATICCONTROL, Rect(aIDENT, aIDENT, aIDENT, aIDENT), "frame", STYLE_FRAME) 
    self.d.AddControl(STATICCONTROL, Rect(aIDENT2, aIDENT2, aAUTO, aAUTO), "label1", STYLE_LABEL, "") 
    self.d.AddControl(EDITCONTROL, Rect(100, aNEXT, aIDENT2, aAUTO), "suffix", STYLE_EDIT, "Enter Suffix:")

    self.suffix = ""

  def on_suffix(self, code):
    self.d.GetValue("suffix")
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

import random


font = fl.font
glyphs = font.glyphs
patternList=[]

#busca sufijo
for index in range(len(glyphs)):
	gl=glyphs[index].name
	if gl == suffix+'.001':
		for n in range(20):
			newValue=suffix+"."+str(n+1).zfill(3)
			if font[newValue] is not None:
				patternList.append(newValue)
			else:
				break

patternCount=len(patternList)
if patternCount > 0:
	for pat in patternList:
		if font[pat] is None:
			fl.Message(pat+" is not a valid and existing glyph pattern. You must declare valid patterns in patternList to make this script work")
			error="si"
	
	def process(g, index, error):
		if g is not None and error=="no":
			for pat in patternList:
				if pat==g.name:
					error="si"
					print "Warning: "+pat+" is a pattern. Glyph patterns won't be applied to themselves."
	
			if error=="no":
				fl.SetUndo(index)
				rand=fl.Random(0, patternCount)
				patternName=patternList[rand]
				pattern=font[patternName]
				#pattern.mark=500
				g.Bsubtract(pattern)
				g.RemoveOverlap()
				g.mark=200
				fl.UpdateGlyph(index)
				#print g.name+" < "+pattern.name
				return 1
				
	if suffix!="":
		for index in range(len(glyphs)):
			if fl.Selected(index) and index!=fl.iglyph:
				process(glyphs[index], index, error)
			elif index == fl.iglyph:	
				process(glyphs[fl.iglyph], fl.iglyph, error)
			fl.UpdateGlyph(index)
	else:
		fl.Message("No suffix entered.")

elif suffix=="":
	fl.Message("No sufix entered. No changes made.")
else:
	fl.Message("There is no pattern glyphs starting from "+suffix+".001. No changes made.")
