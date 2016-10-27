#FLM: AT DEVA Lohit names to Glyphs
from robofab.world import CurrentFont

f=CurrentFont()
output=''
def removeDeva(name):
	newName=name.replace("deva", '')
	return newName

def removeVirama(name):
	newName=name.replace("a_virama", '')
	return newName

def rebuild(partes):
	name=''
	for parte in partes:
		name+=parte+'_'
	return name

def resuffix(name):
	if name.find('.')>0:
		pos=name.find('.')
		pre=name[:pos]
		suf=name[pos:]
		name=pre+'-deva'+suf
	else:
		name=name+'-deva'
	return name

def removeCjctVocal(name):
	if name[-1]=='_':
		name=name[:-1]
	if "a_" in name and "virama_" not in name:
		name=name.replace("a_", '_')
	return name

def Matra(name):
	name=name.replace("sign", 'Matra')
	return name

def reph(name):
	name=name.replace("Matra_r", 'Matra_reph')
	name=name.replace("r_anusvara", 'reph_anusvara')
	if name=='r':
		name='reph'
	return name

def caps(name):
	name=name.replace("short", 'Short')
	name=name.replace("Shortsign", 'ShortMatra')
	name=name.replace("bindu", 'Bindu')
	name=name.replace("vocalic", 'Vocalic')
	return name

def combining(name):
	if 'combiningdigit' in name:
		name=name.replace("combiningdigit", '')
		name+='.comb'
	if 'combiningletter' in name:
		name=name.replace("combiningletter", '')
		name+='.comb'
	if 'candraBindu' in name and len(name)>len('candraBindu_deva') and name[:6]=='candra':
		name=name.replace("candraBindu", 'candraBindu_')
	if 'candraBindu_digit' in name:
		name=name.replace("candraBindu_digit", 'candraBindu_')
	return name

def other(name):
	name=name.replace("candraBinduinverted", 'invertedCandraBindu')
	name=name.replace("yaheavy", 'jjya')
	name=name.replace("candra-deva", 'Candra-deva')
	name=name.replace("candraMatra-deva", 'CandraMatra-deva')
	if '_viraam_' in name:
		name=name.replace('_viraam_','_')
	name=name.replace("virama-deva", 'halant-deva')
	name=name.replace("virama_ra-deva", 'rakar-deva')
	name=name.replace('vattu_ulow-deva','rakar_uMatra-deva')
	name=name.replace('vattu_uulow-deva','rakar_uuMatra-deva')
	return name

def locl(name):
	name=name.replace(".mr", '.loclMAR')
	name=name.replace(".np", '.loclNEP')
	return name

def convert(name):
	newName=''
	newName=removeDeva(name)
	newName=removeVirama(newName)
	newName=removeCjctVocal(newName)
	newName=Matra(newName)
	newName=reph(newName)
	newName=resuffix(newName)
	newName=caps(newName)
	newName=combining(newName)
	newName=other(newName)
	newName=locl(newName)

	return newName

def condition(name):
	if 'virama' in name:
		return True
	elif 'deva' in name:
		return True
	else:
		return False

output=''
lista=[]

for g in f:
	if condition(g.name)==True:
		f[g.name].mark=100
		lista.append([convert(g.name),g.unicode,g.name])
	else:
		f[g.name].mark=5


lista.sort()
array=[]
for item in lista:
	if 'alt' not in item:
		if item[1]:
			item[1]=str(hex(item[1]))[2:]
			item[1]=item[1].zfill(4)
			item[1]=item[1].title()
		output+=str(item[1])+' - '+item[0]+' - '+item[2]+"\n"
		array.append([item[1],item[2],item[0]])
		#output+=str(item[0])+"\n"
#print output
print array
f.update()
