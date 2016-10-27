#FLM: AT URL file
import urllib
f = urllib.urlopen('http://www.andrestorresi.com.ar/test.txt')
readdata = f.read()
readdata2 = unicode( readdata, "iso-8859-1" )
f.close()
print readdata2
