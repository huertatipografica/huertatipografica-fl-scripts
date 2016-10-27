#FLM: AT Hebrew Unicode Batch
#By Andres Torresi
#http://www.huertatipografica.com.ar
#Coded for Zvika Rosenberg

#BACKUP YOUR FILES BEFORE RUNNING THIS SCRIPT!

#configure

#Source directory
fontDir='/Users/Telex/store/tipografia/zvika/'
#Destination dir. Must be an existing directory different from source.
saveDir='/Users/Telex/store/tipografia/zvika/newfiles'

#prefix for new files
#Empty prefix will mantain original name
#prefix=''
prefix='_new_'

#list of unicodes
#VERY IMPORTANT
#ALWAYS alternate unicode(odd) followed with glyph name(even), separated with commas
#The script will find the name of the glyph and assign the unicode in the PREVIOUS item.
unicodesList=[
"fb1f","yod_yod_patah"
,"fb20","alt_ayin"
,"fb21","wide_alef"
,"fb22","wide_dalet"
,"fb23","wide_he"
,"fb24","wide_kaf"
,"fb25","wide_lamed"
,"fb26","wide_mem"
,"fb27","wide_resh"
,"fb28","wide_tav"
,"fb29","uniFB29"
,"fb2a","shin_shindot"
,"fb2b","shin_sindot"
,"fb2c","shin_shindot_dagesh"
,"fb2d","shin_sindot_dagesh"
,"fb2e","alef_patah"
,"fb2f","alef_qamats"
,"fb30","alef_hiriq"
,"fb31","bet_dagesh"
,"fb32","gimel_dagesh"
,"fb33","dalet_dagesh"
,"fb34","he_dagesh"
,"fb35","vav_dagesh"
,"fb36","zayin_dagesh"
,"fb38","tet_dagesh"
,"fb39","yod_dagesh"
,"fb3a","final_kaf_dagesh"
,"fb3b","kaf_dagesh"
,"fb3c","lamed_dagesh"
,"fb3e","mem_dagesh"
,"fb40","nun_dagesh"
,"fb41","samech_dagesh"
,"fb43","final_pe_dagesh"
,"fb44","pe_dagesh"
,"fb46","tsadi_dagesh"
,"fb47","qof_dagesh"
,"fb48","resh_dagesh"
,"fb49","shin_dagesh"
,"fb4a","tav_dagesh"
,"fb4b","vav_holam"
,"fb4c","bet_rafe"
,"fb4d","kaf_rafe"
,"fb4e","pe_rafe"
,"fb4f","alef_lamed"
,"db86","alef_lamed_tsere"
,"db87","alef_lamed_segol"
,"db88","alef_lamed_hatafseg"
,"db8d","alef_dagesh"
,"db8f","alt_lamed"
,"db90","hatafsegol_meteg"
,"db91","hatafpatah_meteg"
,"db92","hatafqamats_meteg"
,"db93","sheva_na"
,"dba0","alef_dag_hazak"
,"dba1","bet_dag_hazak"
,"dba2","gimel_dag_hazak"
,"dba3","dalet_dag_hazak"
,"dba4","vav_dag_hazak"
,"dba5","zayin_dag_hazak"
,"dba6","tet_dag_hazak"
,"dba7","yod_dag_hazak"
,"dba8","fina_kaf_dag_hazak"
,"dba9","kaf_dag_hazak"
,"dbaa","lamed_dag_hazak"
,"dbab","mem_dag_hazak"
,"dbac","nun_dag_hazak"
,"dbad","samech_dag_hazak"
,"dbae","final_pe_dag_hazak"
,"dbaf","pe_dag_hazak"
,"dbb0","tsadi_dag_hazak"
,"dbb1","qof_dag_hazak"
,"dbb2","resh_dag_hazak"
,"dbb3","shin_dag_hazak"
,"dbb4","tav_dag_hazak"
,"dbb5","lamed_hol_dag_hazak"
,"dbb6","shin_shd_dag_hazak"
,"dbb7","shin_sd_dag_hazak"
]


#### FUNCTIONS

def hex2dec(s):
    #return hexadecimal string
    return int(s, 16)

def fixUnicodes(font,myGlyphs):
    par=1
    uniList=[]
    namesList=[]
    for g in myGlyphs:
    		g.mark=0
        if par==0:
            par=1
            namesList.append(g)
        elif par==1:
            par=0
            uniList.append(g)

    for g in font.glyphs:
        g.mark=0
        if g.unicodes==[]:
            g.mark=255
            if g.name in myGlyphs:
                index=myGlyphs.index(g.name)
                glyphname=myGlyphs[index]
                uni=myGlyphs[index-1]
                uni=hex2dec(uni)
                g.unicodes=[uni]
                g.mark=100
            fl.UpdateGlyph(g.index)


def getFiles(path):
    files = []
    for fileName in os.listdir(path):
        base, ext = os.path.splitext(fileName)
        if ext.lower() == ".vfb":
            files.append([base,ext])
    return files


### SCRIPT

import os
import sys
import re
from FL import *

if __name__ == "__main__":

    #close opened files
    flist=len(fl)
    for index in range(flist):
        fl.Close(0)


            #add slash to dir path
    if fontDir[len(fontDir)-1]!='/':
        fontDir=fontDir+'/'
    if saveDir[len(saveDir)-1]!='/':
        saveDir=saveDir+'/'

    #check directories
    error=False
    if fontDir==saveDir:
        print "fontDir and saveDir must be different directories."
        error=True

    if os.path.isdir(fontDir)==False:
        print 'The path to source directory is wrong or doesnt exist. '+fontDir
        error=True

    if saveDir=='':
        print 'You must enter a value for saveDir'
        error=True
    elif os.path.isdir(saveDir)==False:
        print 'The path to destination directory is wrong or doesnt exist. '+saveDir
        error=True


    if error==False:
        files=getFiles(fontDir)
        for file in files:
            filename=file[0]+file[1]
            newfilename=prefix+file[0]+file[1]
            fl.Open(fontDir+filename)
            fixUnicodes(fl.font,unicodesList)
            fl.Save(saveDir+newfilename)
            fl.Close(fl.ifont)
        print 'Done!'
    else:
        print 'There was an error. Nothing was done.'
