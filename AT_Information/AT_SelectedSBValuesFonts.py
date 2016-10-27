#FLM: AT Fonts SB consistence
# Copy the selected widths to other fonts
from robofab.world import CurrentFont,AllFonts,CurrentGlyph
fonts=AllFonts()
forigen=CurrentFont()
sel=forigen.selection

def copiaWidth(myWidth,gtarget):
	anchoFinal=gtarget.width
	anchoActual=myWidth
	anchoDif=anchoActual-anchoFinal
	anchoSide=anchoDif/2
	gtarget.leftMargin=gtarget.leftMargin+anchoSide
	gtarget.rightMargin=gtarget.rightMargin+anchoSide
	gtarget.width=myWidth
	print str(myWidth) + " > " + str(gtarget.width)


def inconsistent(list):
	result=False
	for i in range(len(list)):
		if i>0:
			if list[i-1]<list[i]:
				result=True
	return result

incList=[]

for gname in sel:
	lsb = []
	rsb = []
	width = []
	for f in fonts:
		if gname in f:
			destino=f[gname]	
			lsb.append(destino.leftMargin)
			rsb.append(destino.rightMargin)
			width.append(destino.width)
			#destino.mark=origen.mark
			#copiaWidth(origen.width,destino)
	
	print gname
	if inconsistent(lsb) or inconsistent(rsb):
		print 'INCONSISTENT'
		incList.append(gname)
	print "LSB"
	print lsb
	print "RSB"
	print rsb
	print "WIDTH"
	print width
	print ""
			#f.update()

output=''
print 'Weight Inconsistences: '
for item in incList:
	output += '/'+item+' '
print output
print 'Done.'
