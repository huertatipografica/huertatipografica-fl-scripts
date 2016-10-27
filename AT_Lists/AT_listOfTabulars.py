#FLM: AT List of specific width
from robofab.world import CurrentFont

f = CurrentFont()
output = ''
for gname in f.selection:
	if f[gname].width == 1000:
		output += "'"+gname+"',"
	else:
		f[gname].mark=150

print output
