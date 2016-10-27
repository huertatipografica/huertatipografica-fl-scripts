#FLM: AT URL key
import urllib
f = urllib.urlopen('http://www.andrestorresi.com.ar/key.txt')
readdata = f.read()
#readdata2 = unicode( readdata, "iso-8859-1" )
f.close()
if readdata==str(25277628):
	return True
else:
	return 'Error.'
