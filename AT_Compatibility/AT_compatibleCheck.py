#FLM: AT Compatible through fonts
"""correctDirection(): correct the direction of all contours in this glyphs.
autoContourOrder(): automatically order the contours based on (in this order): the point count of the contours, the segment count of the contours, the x value of the center of the contours, the y value of the center of the contours and the surface of the bounding box of the contours.
"""
from robofab.world import CurrentFont,AllFonts

fonts = AllFonts()
current = CurrentFont()
currentFullName = current.info.fullName

def checkGlyph(g):
	for f in fonts:
		if f[g.name] and f.info.fullName!=currentFullName:
			if g.isCompatible(f[g.name]):
				g.mark=20

for g in current:
	checkGlyph(g)

current.update()
