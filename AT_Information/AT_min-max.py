#FLM: AT Min/Max points
from robofab.world import CurrentFont

f=CurrentFont()

top=0
bottom=10000
output=''
for g in f:
	if g.selected:
		gtop=g.box[3]
		gbot=g.box[1]
		if gtop>top:
			top=gtop
			maxg=g.name
		if gbot<bottom:
			bottom=gbot
			ming=g.name

print maxg,top
print ming,bottom
