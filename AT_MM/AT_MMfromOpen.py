#FLM: AT MM from open font (weight axis)
# Version 1.0
# Duplicates current font, add a new weight axis and opens AssignMaster menu to select and assign the second master.
# By Andres Torresi

#Imports
from robofab.world import CurrentFont
from robofab.interface.all.dialogs import GetFolder, Message, OneList, AskYesNoCancel, AskString, ProgressBar

#Functions
def copyFont():
	tempFont = fl.font
	f = Font(tempFont)
	if tempFont.ot_classes:
		f.ot_classes = tempFont.ot_classes
	if tempFont.features:
		otFeatures = tempFont.features
		for fontFeature in otFeatures:
			f.features.append(Feature(fontFeature))
	fl.Add(f)

#Program
copyFont()
font = fl.font
font.DefineAxis('Weight', 'Weight', 'Wt')
fl.CallCommand(fl_cmd.ToolsAssignMaster)
