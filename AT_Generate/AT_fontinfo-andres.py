#FLM: AT Font Info: Andres Torresi

#configurar

nombreFamilia='Tagoni'
nombreDisenador='Andres Torresi'
emailDisenador='andres@huertatipografica.com.ar'
urlDisenador='http://www.andrestorresi.com.ar'
urlDistribuidor='http://www.huertatipografica.com.ar'
year='2012'

##

from robofab.world import CurrentFont
# all the foundry settings tools live here:
import time

# You will need a font open in fontlab for this demo
font = CurrentFont()
# Let's get the current year so that the year string is always up to date
font.info.year = time.gmtime(time.time())[0]

# Apply those settings that we just loaded
font.info.copyright = 'Copyright (c) '+year+' '+nombreDisenador+' ('+emailDisenador+'), with Reserved Font Name "'+nombreFamilia+'"'
font.info.trademark = nombreFamilia+' is a trademark of '+nombreDisenador+''
font.info.openTypeNameLicense = 'This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: http://scripts.sil.org/OFL'
font.info.openTypeNameLicenseURL = 'http://scripts.sil.org/OFL'
font.info.openTypeNameDescription = ''
font.info.openTypeOS2VendorID = ''
font.info.openTypeNameManufacturerURL = urlDistribuidor
font.info.openTypeNameDesigner = nombreDisenador
font.info.openTypeNameDesignerURL = urlDisenador
# and call the update method
#print "Done"

font.update()

#fl part
#f = fl.font
#print f.copyright
#print f.year
#print f.customdata
#fl.UpdateFont(-1)
