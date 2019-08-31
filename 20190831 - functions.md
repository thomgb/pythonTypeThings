### Things said and done; Part1

**functions** are pieces of code that can take <u>one, more of no arguments</u>. Functions are handy if this piece of code needs to be used multiple times. A function is created with the keyword **def**, then the name of the function, followed by parenthesis with the arguments.

some examples:

``` python
def addTen(value):
	sum = 10 + value
	return sum
```

``` python
# try this in DrawBot
def circle(x, y, radius):
    oval(x-radius, y-radius, radius*2, radius*2)
```


``` python
# try this in DrawBot
def borderedNewPage(margin=30, page="A4"):
    newPage(page)
    pageWidth, pageHeight = sizes(page)
    save()
    fill(.9, .1, .3)
    rect(0, 0, pageWidth, pageHeight)
    fill(1)
    rect(margin, margin, pageWidth-margin*2, pageHeight-margin*2)
    restore()
```

In the last example you see that the arguments are already have values. This is sort of a default. 
They can be overwritten:

``` python
# try this in DrawBot
borderedNewPage(page="A5Landscape")
borderedNewPage(margin=12)
borderedNewPage(margin=20, page="screen")
```

--
next step: classes