#FLM: AT Random string
import random
font = fl.font
glyphs = font.glyphs
i = 0
output=""
while i<1000:
	glyph = random.choice(glyphs)
	index = glyph.index
	if fl.Selected(index):
		output=output+"/"+glyph.name
		i=i+1

print output
