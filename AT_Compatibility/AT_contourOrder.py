#FLM: AT Contour order + direction
"""correctDirection(): correct the direction of all contours in this glyphs.
autoContourOrder(): automatically order the contours based on (in this order): the point count of the contours, the segment count of the contours, the x value of the center of the contours, the y value of the center of the contours and the surface of the bounding box of the contours.
"""
from robofab.world import CurrentFont

for g in CurrentFont():
	g.autoContourOrder()
	g.correctDirection()
