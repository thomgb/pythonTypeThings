from fontParts.world import *

fontPath = "mogeefont.ufo"
word = "HappyBirthday"
strokeThickness = 5
numFramesPerSide = 10

def drawGlyph(glyph):
	from fontTools.pens.cocoaPen import CocoaPen
	pen = CocoaPen(glyph.getParent())
	glyph.draw(pen)
	drawPath(pen.path)
	
def easeInOutQuad(t):
    t *= 2
    if t < 1:
        return 0.5 * (t ** 2)
    else:
        t = 2 - t
        return 1 - 0.5 * (t ** 2)	

# get the font 
font = OpenFont(fontPath, showInterface=False)

# calaculate the canvas
width = 300
height = font.info.unitsPerEm + 200
for letter in word:
    glyph = font[letter]
    width += glyph.width
    
# based on https://gist.github.com/justvanrossum/5bd077104032a42d4bd432d3bdc1dcf7    

for side in range(4):
    for frame in range(numFramesPerSide):
        t = easeInOutQuad(frame / numFramesPerSide)
        newPage(width,height)
        frameDuration(1/20)
        fill(1)
        rect(0, 0, width, height)
        translate(0, -font.info.descender+100)
        fill(0)
        stroke(1)
        strokeWidth(1 * strokeThickness)
        for letter in word:
            if letter == 'B':
                translate(200)
            glyph = font[letter]
            for contour in glyph.contours:
                (x, y, xMax, yMax) = contour.bounds                
                sqSize = xMax - x
                for i in range(5):
                    rect(x + strokeThickness/2, y + strokeThickness/2, sqSize - strokeThickness, sqSize - strokeThickness)

                    if side == 0:
                        dx = 1 + t
                        dy = 1
                    elif side == 1:
                        dx = 2
                        dy = 1 + t
                    elif side == 2:
                        dx = 2 - t
                        dy = 2
                    elif side == 3:
                        dx = 1
                        dy = 2 - t
                    x += dx * strokeThickness
                    y += dy * strokeThickness
                    sqSize -= 3 * strokeThickness
            translate(glyph.width)

saveImage("HappyBirthdayPetra.gif")