#FLM: AT Adjust to grid
from robofab.world import CurrentFont,CurrentGlyph

def standarize(g):
	value=8
	newVal=g.leftMargin/value
	g.leftMargin=newVal*value

	for c in g:
		for p in c.points:
			if p.type!='offcurve':
				newVal=p.x/value
				p.x=newVal*value
				newVal=p.y/value
				p.y=newVal*value

	newVal=g.rightMargin/value
	g.rightMargin=newVal*value

f=CurrentFont()
for g in f:
	if g.selected:
		standarize(g)
		print g

f.update()
