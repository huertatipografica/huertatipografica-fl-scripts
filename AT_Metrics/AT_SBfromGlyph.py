#FLM: AT SBs from glyph

from robofab.world import CurrentFont,CurrentGlyph
from robofab.interface.all.dialogs import Message, ProgressBar, AskYesNoCancel, TwoChecks, AskString
import string

#Program
def check(font,name):
	result = False
	for g in font.glyphs:
		if g.name == name:
			result = True
	return result

font = CurrentFont()
cglyph = CurrentGlyph()
sb = AskString('SB values')
values = sb.split(',')



if check(font,values[0]):
	valueL=font[values[0]].leftMargin
else:
	valueL = cglyph.leftMargin
if check(font,values[1]):
	valueR=font[values[1]].rightMargin
else:
	valueL = cglyph.rightMargin

if valueL == 0:
	valueL = cglyph.leftMargin
if valueR == 0:
	valueR = cglyph.rightMargin

print valueL,valueR
cglyph.leftMargin = valueL
cglyph.rightMargin = valueR
font.update()
