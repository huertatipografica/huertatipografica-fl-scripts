#FLM: AT Kern check for scripts
# Description:
# After declare equivalent glyphs for other script,
#the script copy all the latin kerning combinations to the equivalent script combinations on the lists
#when and outputs a list of changes.

# Credits:
# Andres Torresi. Some parts based on Pablo Impallari's functions

# Dependencies
from robofab.world import CurrentFont

# Clear Output windows
from FL import *
fl.output=""
f = CurrentFont()
kerning = f.kerning

#Declare the kerning equivalences for latin.
eqLatinCy={
'A': 'Acyr',
'H': 'En',
'J': 'Je',
'O': 'Ocyr',
'S': 'Dze',
'T': 'Te',
'X': 'Zhe',
'Y': 'Ucyr',
'i': 'iukrain',
}

eqLatinGr={
'A': 'Alpha',
'H': 'Eta',
'O': 'Theta',
'T': 'Tau',
'X': 'Ha',
'X': 'Chi',
'Y': 'Upsilon',
'Z': 'Zeta',
'Z': 'Sigma',
'h': 'beta',
}

#reads all kerning classes
# def readFontKernClasses(FLfont):
# 	kernClassesNamesList = []
# 	kernClassesDict = {}
# 	classes = FLfont.classes
# 	for c in classes:
# 		sep = c.find(":")
# 		if sep != -1:
# 			cName = str(c[:sep].strip())
# 			cGlyphs = c[sep+1:].strip().split()
# 			if (cName[0] == "_" and len(cGlyphs)):
# 				kernClassesNamesList.append(cName)
# 				kernClassesDict[cName] = cGlyphs
# 	return kernClassesNamesList, kernClassesDict
#
# #returns a list with all the classes keys
# def getClassKeys():
#     kclasses = readFontKernClasses(fl.font)
#     glyphList=[]
#     for kclass in kclasses[1]:
#         glyphList.append(kclasses[1][kclass][0][:-1])
#     return glyphList
#
# #returns true if the glyph name exist as a class key
# def checkKey(gname):
#     result = False
#     if gname in getClassKeys():
#         result = True
#     return result

#returns two lists with index pairs and script pairs
def returnPairs(list):
    basePair=[]
    eqPair=[]
    for left in list:
        for right in list:
            basePair.append((left,right))
            eqPair.append((list[left],list[right]))
    return basePair,eqPair

#return equivalent pairs with different values
def checkPairs(list):
    output=''
    pairList = returnPairs(list)
    for index in range(len(pairList[0])):
        if pairList[0][index] in kerning.keys():
            # print kerning[pairList[0][index]],kerning[pairList[1][index]]

            if kerning[pairList[0][index]]!=kerning[pairList[1][index]] and kerning[pairList[1][index]]:
                value = kerning[pairList[0][index]]
                kerning[pairList[1][index]] = value
                output+='/'+pairList[0][index][0]+'/'+pairList[0][index][1]+' '+str(kerning[pairList[0][index]])+' '
                output+='/'+pairList[1][index][0]+'/'+pairList[1][index][1]+' '+str(kerning[pairList[1][index]])+"\n"
                # print pairList[0][index],kerning[pairsCy[0][index]],pairList[1][index],kerning[pairList[1][index]]
    return output


# You can use the following lines if you want to check each glyph in the lists belongs to a specific script.
# listCyrillic=['Acyr','Be','Ve','Ghe','De','Ie','Zhe','Ze','Icyr','Ka','El','Em','En','Ocyr','Pe','Er','Es','Te','Ucyr','Ef','Ha','Tse','Che','Sha','Shcha','Hard','Yeru','Soft','Ecyr','Yu','Ya','acyr','be','ve','ghe','de','ie','zhe','ze','icyr','ka','el','em','en','ocyr','pe','er','es','te','ucyr','ef','ha','tse','che','sha','shcha','hard','yeru','soft','ecyr','yu','ya','De.loclBGR','El.loclBGR','Ef.loclBGR','be.locl_MKDSRB','ve.locl_BGR','ghe.locl_BGR','de.locl_BGR','zhe.locl_BGR','ze.locl_BGR','icyr.locl_BGR','ka.locl_BGR','el.loclBGR','pe.locl_BGR','te.locl_BGR','tse.locl_BGR','sha.locl_BGR','shcha.locl_BGR','hard.locl_BGR','soft.locl_BGR','yu.locl_BGR','Ieukrain','Iukrain','Je','Dze','Lje','Nje','Tshe','Dje','Dzhe','Gheup','ieukrain','iukrain','je','dze','lje','nje','tshe','dje','dzhe','gheup','Io','Yi','Gje','Kje','Iegrave','Igravecyr','io','yi','gje','kje','iegrave','igravecyr','Ibrevecyr','Ubrevecyr','ibrevecyr','ubrevecyr','ibrevecyr.locl_BGR']
# listGreek=['Alpha','Beta','Gamma','Deltagreek','Epsilon','Zeta','Eta','Theta','Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omegagreek','alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa','lambda','mugreek','nu','xi','omicron','pi','rho','sigma1','sigma','tau','upsilon','phi','chi','psi','omega','anoteleia','questiongreek','numeralsign','lownumeralsign','acutecomb.grek','acutecomb.grek.cap','tonos','dialytikatonoscomb','dieresistonos','Alphatonos','Epsilontonos','Etatonos','Iotatonos','Omicrontonos','Upsilontonos','Omegatonos','Iotadieresis','Upsilondieresis','alphatonos','epsilontonos','etatonos','iotatonos','omicrontonos','upsilontonos','omegatonos','iotadieresis','upsilondieresis','iotadieresistonos','upsilondieresistonos']
# for n in eqLatinCy:
#     if eqLatinCy[n] not in listCyrillic:
#         print eqLatinCy[n]

print checkPairs(eqLatinCy)
print checkPairs(eqLatinGr)

f.update()
