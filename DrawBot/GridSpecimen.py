from fontParts.world import *
import string

fontPath = "IBM Plex Serif-Regular.ufo"

biggies = {
    # glyphName: (1,2,3,4,80) #x,y,w,h,extra(=smaller in the box)
    'A': (1, 0, 2, 3, 250),     
    "uni0414": (4, 2, 2, 3, 240),
    #"Zhecyr": (9, 6, 3, 5, 240),

    # choice(f.keys()): (5, 1,2, 3,120),
}





font = OpenFont(fontPath, showInterface=False)


def drawGlyph(glyph):
    from fontTools.pens.cocoaPen import CocoaPen
    pen = CocoaPen(glyph.getParent())
    glyph.draw(pen)
    drawPath(pen.path)

Variable([
    dict(name="page", ui="PopUpButton",
       
        args=dict(
            items=list(sizes().keys()),
            )),
    dict(name="columns", ui="Slider",
            args=dict( 
                value=7, 
                minValue=1, 
                maxValue=20,
                tickMarkCount = 19,
                stopOnTickMarks=True,
                )),      
    dict(name="rows", ui="Slider",
            args=dict( 
                value=5, 
                minValue=1, 
                maxValue=20,
                tickMarkCount = 19,
                stopOnTickMarks=True,
                )),    
    dict(name="color", ui="CheckBox"),
    dict(name="negative", ui="CheckBox"),
    dict(name="border", ui="Slider",
            args=dict( 
                value=2, 
                minValue=-1, 
                maxValue=20,
                )),        
    dict(name="doBiggies", ui="CheckBox"), 
    dict(name="yCorrection", ui="Slider",
            args=dict( 
                value=2.5, 
                minValue=0, 
                maxValue=5,
                )),  
    dict(name="update", ui="Button")             
                
],globals()) 



# cleanup crew
columns = int(columns)
rows = int(rows)
diap = negative
boxMargin = border
print("rows:   ",rows)
print("columns:", columns)
f = font

gs = list(string.ascii_letters)+['zero','one','two','three','four','five','six','seven','eight','nine']  # just the selection
gs = list(f.keys())     # or all glyphs


w,h = sizes(list(sizes().keys())[page])
newPage(w,h)

if boxMargin > 0:
    save()
    strokeWidth(boxMargin*2)
    fill(None)
    if diap:
        stroke(1)
    else:
        stroke(0)
    rect(0,0,w,h)
    restore()
    w-=boxMargin*2
    h-=boxMargin*2

    translate(boxMargin,boxMargin)
blockWidth = w/columns
blockHeight = h/rows
print("cell size:",blockWidth, blockHeight)
#print 
def big(glyphName, pos):
    
    g = f[glyphName]
    gw= g.box[2]+g.box[0]
    gh = g.box[3]-g.box[1]
    x,y,w,h,a = pos
    bigWidth = w*blockWidth
    bigHeight = h*blockHeight
    save()
    if color:
        r,gr,b = random()*2,random()/1.4,random()/3
        if sum([r,gr,b]) < .4:
            r=.5
            gr=.2
            b=1
        fill(r,gr,b,1)
    else:
        if diap:
            fill(0)
        else:
            fill(1)
    extra = 0
    if diap:
        extra = 0
    
    rect(
            x*blockWidth+boxMargin-extra,
            y*blockHeight+boxMargin-extra,
            w*blockWidth-2*boxMargin+2*extra,
            h*blockHeight-2*boxMargin+2*extra)
    translate(x*blockWidth,y*blockHeight)
    if bigHeight/gh < bigWidth/gw:
        scaleFactor = bigHeight/(gh+a)
    else:
        scaleFactor = bigWidth/(gw+a)
    translate(
            (bigWidth-gw*scaleFactor)/2,
            (-g.box[1]*scaleFactor)+(bigHeight-gh*scaleFactor)/2
            )

    if diap:
        fill(1)
    else:
        fill(0)
    scale(scaleFactor)
    drawGlyph(g)
    restore()

def drawBox(x,y):
    if color:
        r,g,b = random()*2,random()/1.4,random()/3
        if sum([r,g,b]) < .4:
            r=.2
            g=.5
            b=.1
        fill(r,g,b)
    else:
        if diap:
            fill(0)
        else:
            fill(1)
    rect(
            x*blockWidth+boxMargin,
            y*blockHeight+boxMargin,
            blockWidth-2*boxMargin,
            blockHeight-2*boxMargin
            )
    if diap:
        fill(1)
    else:
        fill(0)
    goodGlyph = False
    while not goodGlyph:
        g = f[choice(gs)]
        gs.remove(g.name)
        if g.name not in biggies and g.contours:
            goodGlyph = True
    save()
    translate(x*blockWidth+blockWidth/2,y*blockHeight)
    if blockHeight < blockWidth:
        scaleFactor = blockHeight/1800
    else:
        scaleFactor = blockWidth/1400
    scale(scaleFactor)

    translate(
        (-g.bounds[2]-g.bounds[0])/2,
        blockHeight/scaleFactor/yCorrection+f.info.descender
        )
    drawGlyph(g)
    restore()

if not diap:
    save()
    fill(0)
    rect(0,0,w,h)
    restore()

for x in range(columns):
    for y in range(rows):
        drawBox(x,y)
        
if doBiggies:
    for glyphName, pos in biggies.items():
        big(glyphName, pos)


  
        