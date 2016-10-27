#FLM: AT List diff widths
# Copia los anchos de caja de la fuente seleccionada a las otras fuentes abiertas.
import math
from robofab.world import CurrentFont

refWidth = 405
for gname in f.selection:
	g=f[gname]
	if g.width != newVal:
		print gname
