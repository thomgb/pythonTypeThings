"""
rotate word loop
"""

frames = 200
word = "dontgetdizzy"
_font = "Times"
pageSize = 1000
for frame in range(frames):
    newPage(pageSize, pageSize)
    frameDuration(1/30)
    font(_font, 30)    
    tw,th = textSize(word)
    translate(pageSize/2, pageSize/2)  # center of canvas
    scale(pageSize/(tw+30))

    # you gotta love math!
    # print( sin((2*pi)/frames*frame) )
    # the result of sinus is between -1 and 1
    # 0=0 pi/2=1 pi=1 1.5*pi=-1  2*pi=0 
    # multiply by a factor to give it more swing!
    rotate(sin((2*pi)/frames*frame)*40 )
    
    translate(-pageSize/2,-pageSize/2)  # back to origin
    
    translate(pageSize/2-tw/2,pageSize/2-th/2)  # centered!
    text(word,(0,0))  # draw to word
saveImage("rotateWord.gif") # save