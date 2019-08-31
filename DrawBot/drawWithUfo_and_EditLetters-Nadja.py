"""
example of drawing with a typeface

test

"""


from fontParts.world import *

fontPath = "pixels-smal.ufo"
word = "typeface"
# some functions

def drawGlyph(glyph):
	from fontTools.pens.cocoaPen import CocoaPen
	pen = CocoaPen(glyph.getParent())
	glyph.draw(pen)
	drawPath(pen.path)

# get the font 
font = OpenFont(fontPath, showInterface=False)

# calaculate the canvas
width = 0
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
            point.x += randint(-20,20)
            point.y += randint(-20,20)
    drawGlyph(font[letter])
    translate(glyph.width)

