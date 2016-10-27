#FLM: AT List /selected,
#Need to select the desired glyphs :)

from robofab.world import CurrentFont,CurrentGlyph

f = CurrentFont()
g = CurrentGlyph()
output = ''
for gname in f.selection:
	glyph = f[gname]
	output+= '/'+glyph.name+'/comma'

print output
