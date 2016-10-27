#FLM: AT Ruben Fontana
font=fl.font
glyphs=fl.font.glyphs
signos=len(glyphs)
output="Ruben Fontana dice: "
if signos<256:
	output+="No tienes suficientes signos. ("+str(signos)+" de 256). A trabajar, vagos!"
else:
	output+="Suficientes signos. ("+str(signos)+")."

print output
