import turtle
from turtle import *

turtle.setup(400,400)
turtle.bgcolor('green')
turtle.title('Mouse Exercise')

lukaku = turtle.Turtle()
lukaku.shape("turtle")
lukaku.penup()
lukaku.goto(0, 150)
lukaku.pendown()
style = ('verdana', 10, 'italic')
lukaku.color('white', 'purple')
lukaku.write("Programmer:-Mr.Olayinka-Goodluck \nStudent:-ID-2144303.", font=style, align='center' )

kepa = turtle.Turtle()
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,0)
kepa.pendown()
kepa.color('white','brown')


#draw square
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(0, 120)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.fd(100)

def clickleft(x, y):
    lukaku.lt(90)
    
def clickmiddle(x, y):
    lukaku.rt(90)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")

#draw rectangle
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(-120, 120)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.fd(100)

def clickleft(x, y):
    lukaku.lt(90)
    
def clickmiddle(x, y):
    lukaku.rt(90)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")

#draw triangle
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(-120, 120)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.fd(100)

def clickleft(x, y):
    lukaku.lt(120)
    
def clickmiddle(x, y):
    lukaku.rt(120)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")


#draw circle
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(0, 50)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.circle(50)

def clickleft(x, y):
    lukaku.circle(50)
    
def clickmiddle(x, y):
    lukaku.circle(50)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")

#draw pentagon
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(0, 50)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.fd(50)

def clickleft(x, y):
    lukaku.lt(72)
    
def clickmiddle(x, y):
    lukaku.rt(72)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")

#draw hexagon
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(0, 50)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.fd(50)

def clickleft(x, y):
    lukaku.lt(60)
    
def clickmiddle(x, y):
    lukaku.rt(60)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")

#draw heptagon
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(0, 50)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.fd(50)

def clickleft(x, y):
    lukaku.lt(51.4)
    
def clickmiddle(x, y):
    lukaku.rt(51.4)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")

#draw octagon
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(0, 50)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.fd(50)

def clickleft(x, y):
    lukaku.lt(45)
    
def clickmiddle(x, y):
    lukaku.rt(45)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")

#draw nonagon
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(-120, 80)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.fd(50)

def clickleft(x, y):
    lukaku.lt(40)
    
def clickmiddle(x, y):
    lukaku.rt(40)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")

#draw decagon
lukaku.penup()
lukaku.shape('turtle')
lukaku.goto(-120, 80)
lukaku.pendown()
lukaku.color('white', 'purple')
def clickright(x, y):
    lukaku.fd(50)

def clickleft(x, y):
    lukaku.lt(36)
    
def clickmiddle(x, y):
    lukaku.rt(36)

def exit_close():
    exit()

lukaku.onclick(clickright, 3)
lukaku.onclick(clickleft, 1)
lukaku.onclick(clickmiddle, 2)
onkeypress(exit_close, "x")




#draw square
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.fd(100)

def clickleft(x, y):
    kepa.lt(90)
    
def clickmiddle(x, y):
    kepa.rt(90)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")

#draw rectangle
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.fd(100)

def clickleft(x, y):
    kepa.lt(90)
    
def clickmiddle(x, y):
    kepa.rt(90)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")

#draw triangle
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.fd(100)

def clickleft(x, y):
    kepa.lt(120)
    
def clickmiddle(x, y):
    kepa.rt(120)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")

#draw circle
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.circle(50)

def clickleft(x, y):
    kepa.circle(50)
    
def clickmiddle(x, y):
    kepa.circle(50)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")

#draw pentagon
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.fd(50)

def clickleft(x, y):
    kepa.lt(72)
    
def clickmiddle(x, y):
    kepa.rt(72)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")

#draw hexagon
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.fd(50)

def clickleft(x, y):
    kepa.lt(60)
    
def clickmiddle(x, y):
    kepa.rt(60)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")

#draw heptagon
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.fd(50)

def clickleft(x, y):
    kepa.lt(51.4)
    
def clickmiddle(x, y):
    kepa.rt(51.4)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")

#draw octagon
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.fd(50)

def clickleft(x, y):
    kepa.lt(45)
    
def clickmiddle(x, y):
    kepa.rt(45)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")

#draw nonagon
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.fd(50)

def clickleft(x, y):
    kepa.lt(40)
    
def clickmiddle(x, y):
    kepa.rt(40)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")

#draw decagon
kepa.shape("turtle")
kepa.penup()
kepa.goto(0,-150)
kepa.pendown()
kepa.color('white','brown')
def clickright(x, y):
    kepa.fd(50)

def clickleft(x, y):
    kepa.lt(36)
    
def clickmiddle(x, y):
    kepa.rt(36)

def exit_close():
    exit()

kepa.onclick(clickright, 2)
kepa.onclick(clickleft, 1)
kepa.onclick(clickmiddle, 3)
onkeypress(exit_close, "x")










turtle.listen()


# lukaku.hideturtle()


turtle.mainloop()





turtle.done()