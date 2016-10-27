#FLM: AT rename (!)
from robofab.world import CurrentFont
string1='findText'
string2='replaceText'

f = CurrentFont()
for gname in f.selection:
	#f[gname]
	newname=gname.replace(string1,string2)
	f[gname].name = newname

f.update()