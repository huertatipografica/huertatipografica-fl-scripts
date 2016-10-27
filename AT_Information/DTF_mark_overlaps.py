#FLM: DTF Mark Overlaps
# Mark Glyphs Containing Overlaps
#
# This script checks glyphs for overlaps. 
# It works on simple glyphs and glyphs that include components.
#
# Copyright 2011 James Puckett, jp@dunwichtype.com
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


from robofab.world import CurrentFont
font = CurrentFont()

#Copy a glyph and then delete it

for glyph in font:
	# Only proceed if glyph has contours
	if len(glyph) != 0:

		#initialize counters
		glyphAnchors = 0
		copyAnchors = 0

		# Make the first copy
		newname = glyph.name
		newname += ".tmp1"
		copy = font.insertGlyph(glyph, newname)

		# Make the second copy
		newname = glyph.name
		newname += ".tmp2"
		copyTwo = font.insertGlyph(glyph, newname)

		#Decompose any composites in the copies
		for c in copy.components:
			counter = 0
			copy.components[counter].decompose()
			counter +=  1

		for c in copyTwo.components:
			counter = 0
			copyTwo.components[counter].decompose()
			counter +=  1

		#Remove overlaps in the second copy
		copyTwo.removeOverlap()

		#Generate string from anchor points of contours in copy
		origBlob = "0"
		for contour in copy:
			for eachPoint in contour.bPoints:
				for eachAnchor in eachPoint.anchor:
					origBlob += `eachAnchor`
		oneHash = hash(origBlob)

		#Generate string from anchor points of contours in copyTwo
		copyBlob = "0"
		for contour in copyTwo:
			for eachPoint in contour.bPoints:
				for eachAnchor in eachPoint.anchor:
					copyBlob += `eachAnchor`
		#print blob
		twoHash = hash(copyBlob)

		#Mark glyph red if it contains overlaps
		if oneHash != twoHash:
			glyph.mark = 255

		#Delete the copies
		nameOne = copy.name
		nameTwo = copyTwo.name
		font.removeGlyph(nameOne)
		font.removeGlyph(nameTwo)

font.update()
print "Finished checking for and marking overlaps."
