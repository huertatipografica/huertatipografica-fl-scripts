#FLM: AT List /noHOon
from robofab.world import CurrentFont

output = ""
font = CurrentFont()
for gname in font.selection:
	output = output + "/"+gname +  " noHOon"

print output
