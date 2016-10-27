#FLM: Copiar Kerning UC->LC
from robofab.world import CurrentFont
font = CurrentFont()
kerning = font.kerning
Caps=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Lc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#for left, right in kerning.keys():
#    print left, right, kerning[(left, right)]
for left, right in kerning.keys():
	print left, right, kerning[(left, right)]
	print left.lower(), right.lower(), kerning[(left, right)]
	kernValue=kerning[(left, right)]
	kerning[(left.lower(), right.lower())]=kernValue
	kerning[(left.lower(), right)]=kernValue
	kerning[(left, right.lower())]=kernValue