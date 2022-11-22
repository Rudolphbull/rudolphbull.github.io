import turtle                
from turtle import *        

turtle.setup(300,400)
turtle.bgcolor('blue')
turtle.title('Keypress Exercise')

lukaku = turtle.Turtle()
lukaku.shape("turtle")
lukaku.penup()
lukaku.goto(0, 150)
lukaku.pendown()
style = ('verdana', 10, 'italic')
lukaku.color('white')
lukaku.write("Programmer:-Mr.Olayinka-Goodluck \nStudent:-ID-2144303.", font=style, align='center' )


#draw square
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(-120, 0)
lukaku.pendown()
lukaku.color('purple')

def move_forward():
    lukaku.fd(70)

def move_left():
    lukaku.lt(90)
    
    
def move_right():
    lukaku.rt(90)
    

def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")

#draw rectangle
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(0, -120)
lukaku.pendown()
lukaku.color('purple')
def move_forward():
    lukaku.fd(100)

def move_left():
    lukaku.lt(90)
    
def move_right():
    lukaku.rt(90)
    
def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")


#draw triangle
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(0, -120)
lukaku.pendown()
lukaku.color('gold')
def move_forward():
    lukaku.fd(100)

def move_left():
    lukaku.lt(120)
    
def move_right():
    lukaku.rt(120)
    
def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")


#draw circle
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(0, -100)
lukaku.pendown()
lukaku.color('violet')
def move_forward():
    lukaku.circle(120)

def move_left():
    lukaku.circle(90)
    
    
def move_right():
    lukaku.circle(90)
    

def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")


#draw pentagon
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(0, 90)
lukaku.pendown()
lukaku.color('indigo')
def move_forward():
    lukaku.fd(100)

def move_left():
    lukaku.lt(72)
    
    
def move_right():
    lukaku.rt(72)
    

def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")


#draw hexagon
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(90, 0)
lukaku.pendown()
lukaku.color('indigo')
def move_forward():
    lukaku.fd(100)

def move_left():
    lukaku.lt(60)
    
    
def move_right():
    lukaku.rt(60)
    

def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")


#draw heptagon
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(90, 0)
lukaku.pendown()
lukaku.color('indigo')
def move_forward():
    lukaku.fd(100)

def move_left():
    lukaku.lt(51.4)
    
    
def move_right():
    lukaku.rt(51.4)
    

def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")


#draw octagon
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(90, 0)
lukaku.pendown()
lukaku.color('red')
def move_forward():
    lukaku.fd(50)

def move_left():
    lukaku.lt(45)
    
    
def move_right():
    lukaku.rt(45)
    

def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")


#draw nonagon
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(90, 0)
lukaku.pendown()
lukaku.color('orange')
def move_forward():
    lukaku.fd(50)

def move_left():
    lukaku.lt(40)
    
    
def move_right():
    lukaku.rt(40)
    

def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")


#draw decagon
lukaku.shape('turtle')
lukaku.penup()
lukaku.goto(0, 0)
lukaku.pendown()
lukaku.color('green')
def move_forward():
    lukaku.fd(50)

def move_left():
    lukaku.lt(36)
    
    
def move_right():
    lukaku.rt(36)
    

def exit_close():
    exit()

onkeypress(move_forward, "Up")
onkeypress(move_right, "Right")
onkeypress(move_left, "Left")
onkeypress(exit_close, "x")



turtle.listen()


# lukaku.hideturtle()





turtle.mainloop()


turtle.done()