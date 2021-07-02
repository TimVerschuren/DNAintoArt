from tkinter.colorchooser import askcolor
from time import sleep
import math
import turtle

def box(intDim):
    myPen.begin_fill()
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.left(90)
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)

x = 0

print("Welcome to the DNAintoArtinator!")
sleep(1)
DNAseq = input("Paste in your DNA sequence here: ")
boxsize = input("Enter size of cubes here (eg. 20): ")

color_A = askcolor(title="Pick a color for A")
color_T = askcolor(title="Pick a color for T")
color_C = askcolor(title="Pick a color for C")
color_G = askcolor(title="Pick a color for G")

DNAlist = list(DNAseq)

area = round(math.sqrt(len(DNAlist)))

myPen = turtle.Turtle()
myPen.speed(0)
myPen.penup()
myPen.forward(-area*((float(boxsize)/2)))
myPen.setheading(90)
myPen.forward(area*((float(boxsize)/2)))
myPen.setheading(0)

for nuc in DNAlist:
    if x < area:
        if nuc == 'A':
            myPen.color(str(color_A[1]))
            box(float(boxsize))
            myPen.forward(float(boxsize))
            x += 1
        elif nuc == 'T':
            myPen.color(str(color_T[1]))
            box(float(boxsize))
            myPen.forward(float(boxsize))
            x += 1
        elif nuc == 'C':
            myPen.color(str(color_C[1]))
            box(float(boxsize))
            myPen.forward(float(boxsize))
            x += 1
        elif nuc == 'G':
            myPen.color(str(color_G[1]))
            box(float(boxsize))
            myPen.forward(float(boxsize))
            x += 1
        else:
            pass
    else:
        myPen.penup()
        myPen.left(270)
        myPen.forward(float(boxsize))
        myPen.left(270)
        myPen.forward(float(boxsize)*area)
        myPen.left(270)
        myPen.setheading(0)
        if nuc == 'A':
            myPen.color(str(color_A[1]))
            box(float(boxsize))
            myPen.forward(float(boxsize))
            x = 1
        elif nuc == 'T':
            myPen.color(str(color_T[1]))
            box(float(boxsize))
            myPen.forward(float(boxsize))
            x = 1
        elif nuc == 'C':
            myPen.color(str(color_C[1]))
            box(float(boxsize))
            myPen.forward(float(boxsize))
            x = 1
        elif nuc == 'G':
            myPen.color(str(color_G[1]))
            box(float(boxsize))
            myPen.forward(float(boxsize))
            x = 1
        else:
            x = 1

myPen.penup()
myPen.forward(2000)
turtle.Screen().exitonclick()
