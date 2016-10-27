#FLM: AT Reset component x on selected
from robofab.world import CurrentFont

font = CurrentFont()
sel = font.selection

for gname in sel:
	if  len(font[gname].components)>0<1:
		if font[gname].components[0].offset[0] != 0:
			x = font[gname].components[0].offset[0]
			y = font[gname].components[0].offset[1]
			print gname,font[gname].components[0].offset
			font[gname].components[0].offset=(0,y)

font.update()
