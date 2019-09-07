# import fontParts, so ufos can by used
from fontParts.world import *

# a drawGlyph functions
# I always just copy/paste this function...
# # its too complicated to remember ;)
def drawGlyph(glyph):
	from fontTools.pens.cocoaPen import CocoaPen
	pen = CocoaPen(glyph.getParent())
	glyph.draw(pen)
	drawPath(pen.path)

# Open a ufo as f
f = OpenFont("../pixels-smal.ufo")

# parameters, whats the word? 
word = list("HappyBday")
# glyphsname longer than 1 character are added
word.insert(5, "space")
word.insert(7, "hyphen")
# print the word
print(word)

# how many frames the whole gif takes?
frames = 10

# the colors
color1 = (0.88, 0.07, 0.56)
color2 = (0.08, 0.35, 0.5)

# calculate the interpolation from 
# color1 to color2, split up by rgb
redStep = ((color2[0]-color1[0])/frames)
greenStep = ((color2[1]-color1[1])/frames)
blueStep = ((color2[2]-color1[2])/frames)

# a function to draws the word at a position
def drawWord(position):
    # position is a x,y coordinate: (10,30) / [10,30]
    save()
    # the * unpacks this 
    translate(*position)
    """
    without *:
    translate(position)
    would be
    translate((10,30))
    which is not good
    we need
    translate(10,30)
    """
    scale(.2)
    for letter in word:
        glyph = f[letter]
        drawGlyph(glyph)
        translate(glyph.width)
    restore()

# 'main' loop
for frame in range(frames):
    newPage(1000,400)
    # every frame gets 1/10 of a second
    frameDuration(1/10)
    fill(1)
    rect(0,0,1000,400)
    # for every new frame make a newPage
    # and give it a white background
    # because gifs are transparent

    for i in range(14): # 14 layers, seems nice :)
        # calculate the color
        step = ((frame+i) % frames)+1
        fill(    color1[0]+redStep*step,
                 color1[1]+greenStep*step,
                 color1[2]+blueStep*step
                 )        
        # draw that word
        drawWord((170-i*10,120+i*5))
    
    # every other frame the top most word is 
    # white or color1 
    if frame % 2 == 0:
        fill(*color1)
        # shadoooow!
        shadow((0,0), 20, (1,1,1))
    else:
        fill(1)
        shadow((0,0), 20, (0.88, 0.07, 0.56))

    drawWord((170-14*10,120+14*5))

# save it as a gif :)
saveImage("hoorah.gif")
# Congrats Petra! 
# Python on!
