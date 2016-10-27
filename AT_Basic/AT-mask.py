#FLM: AT (?) Mask substract
from robofab.world import CurrentFont,CurrentGlyph

g = CurrentGlyph()

n = g.naked()
mask = n.mask

base = f["O"]
cutter = f["a"]
dest = g

dest.appendGlyph(base)
dest.naked().Bsubtract(cutter.naked())

dest.update()
