#FLM: 03. Remove Selected Anchors
# Version 1.0
# por Andres Torresi (http://www.huertatipografica.com.ar)
# Basado en el script de Ben Kiel
# No me hago responsable por problemas derivados del uso de este programa

from robofab.world import CurrentFont
from robofab.interface.all.dialogs import Message

#Program
font = CurrentFont()
glyphs = font.selection
for glyph in glyphs:
	font[glyph].clearAnchors()
font.update()
Message('All done!')
	
