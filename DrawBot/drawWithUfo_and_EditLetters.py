"""
example of drawing with a typeface

"""

# parameters
fontPath = "pixels-smal.ufo"
word = "typeface"
distortion = 20

from fontParts.world import *

# some functions
def drawGlyph(glyph):
	from fontTools.pens.cocoaPen import CocoaPen
	pen = CocoaPen(glyph.getParent())
	glyph.draw(pen)
	drawPath(pen.path)

# get the font 
font = OpenFont(fontPath, showInterface=False)

# calaculate the canvas
width = 100
height = font.info.unitsPerEm + 200
for letter in word:
    glyph = font[letter]
    width += glyph.width

newPage(width,height)
translate(0,-font.info.descender+100)
for letter in word:
    glyph = font[letter]
    for contour in glyph.contours:
        for point in contour.points:
            point.x += randint(-distortion, distortion)
            point.y += randint(-distortion, distortion)
    drawGlyph(font[letter])
    translate(glyph.width)

