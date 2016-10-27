#FLM: AT Copy SB UC->LC
from robofab.world import CurrentFont
font = CurrentFont()
kerning = font.kerning
Caps=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Lc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#for left, right in kerning.keys():
#    print left, right, kerning[(left, right)]
for i in range(len(Caps)):
	font[Lc[i]].leftMargin=font[Caps[i]].leftMargin
	font[Lc[i]].rightMargin=font[Caps[i]].rightMargin
	font[Lc[i]].mark=200

font.update()
