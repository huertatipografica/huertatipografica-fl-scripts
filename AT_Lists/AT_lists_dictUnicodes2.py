#FLM: AT List gname:unicode
from robofab.world import CurrentFont

f = CurrentFont()
output = ''
for gname in f.selection:
	g=f[gname]
	unicode=''
	if g.unicode:
		unicode=str(hex(g.unicode))
		unicode=unicode[2:]
		unicode=unicode.zfill(6)
		unicode=unicode.upper()
	output += "'"+gname+"': '"+unicode[2:]+"',"

print output
