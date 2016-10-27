#FLM: AT Dict of unicode/name

from robofab.world import CurrentFont

f = CurrentFont()
mydict={}

for g in f.selection:
	uni = f[g].unicode
	mydict[uni]=f[g].name

print mydict
