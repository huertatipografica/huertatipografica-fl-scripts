#FLM: AT_Copy First Letter SB
from robofab.world import CurrentFont,CurrentGlyph

f = CurrentFont()
g = CurrentGlyph()

numStart=875

for gname in f.selection:
	glyph = f[gname]
	glyphRef = f[gname[0]]
	if f[gname[0]]:
		glyph.leftMargin = glyphRef.leftMargin
		glyph.rightMargin = glyphRef.rightMargin
		print glyphRef.name
