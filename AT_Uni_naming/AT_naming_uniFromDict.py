#FLM: AT Naming - Change name by uni dict

from robofab.world import CurrentFont

f = CurrentFont()
uni = 189

myunicodes = {8529: 'oneninth', 188: 'onequarter', 189: 'onehalf', 8528: 'oneseventh', None: 'eightninths', 8531: 'onethird', 8532: 'twothirds', 190: 'threequarters', 8534: 'twofifths', 8535: 'threefifths', 8536: 'fourfifths', 8537: 'onesixth', 8538: 'fivesixths', 8539: 'oneeighth', 8540: 'threeeighths', 8541: 'fiveeighths', 8542: 'seveneighths', 8533: 'onefifth'}
for g in f:
	if g.unicode in myunicodes and g.unicode is not None:
		print g.name
		g.name = myunicodes[g.unicode]
		print g.name
		print g.unicode