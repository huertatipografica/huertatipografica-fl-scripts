#FLM: AT Duplicate contours
from robofab.world import CurrentFont
from robofab.interface.all.dialogs import ProgressBar
import collections

f = CurrentFont()
tickCount = len(f)
bar = ProgressBar('Chequeando...', tickCount)
tick = 0
myNodes=[]

for g in f.selection:
	myNodes=[]
	bar.tick(tick)
	tick = tick+1
	for c in f[g]:
		for p in c.points:
			if p.type!='move' and p.type!='offcurve':
				myNodes.append((p.x,p.y))
	myNodes.sort()
	duplicates=[x for x, y in collections.Counter(myNodes).items() if y > 1]
	contNumber=len(f[g])

	if len(duplicates)>contNumber:
		f[g].mark=255
		print f[g].name
		print duplicates
		print '-----'
	else:
		f[g].mark=0
	myNodes=[]

bar.close()
