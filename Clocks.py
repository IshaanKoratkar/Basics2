import turtle
import time

window = turtle.Screen() 
window.title("Clocks") 
window.setup(width = 1000, height = 500) 
window.bgcolor("black") 
window.tracer(0) 

pen = turtle.Turtle() 
pen.hideturtle() 
pen.speed(0) 
pen.pensize(2)  

def analog_clock(hours, minutes, seconds):
    pen.up() 
    pen.goto(0, 210) 
    pen.setheading(180) 
    pen.color("white")
    pen.pendown() 
    pen.circle(210) 
    
    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90) 

    for x in range(12):
        pen.fd(190) 
        pen.pendown() 
        pen.fd(20) 
        pen.penup() 
        pen.goto(0, 0) 
        pen.rt(30) 

    pen.penup() 
    pen.goto(0, 0) 
    pen.color("pink") 
    pen.setheading(90) 
    angle = (hours / 12) * 360
    pen.rt(angle) 
    pen.pendown() 
    pen.fd(160)

    pen.penup() 
    pen.goto(0, 0) 
    pen.color("turquoise") 
    pen.setheading(90) 
    angle = (minutes / 60) * 360
    pen.rt(angle) 
    pen.pendown() 
    pen.fd(100)

    pen.penup() 
    pen.goto(0, 0) 
    pen.color("gray") 
    pen.setheading(90) 
    angle = (seconds / 60) * 360
    pen.rt(angle) 
    pen.pendown() 
    pen.fd(100)

while True:
    hours = int(time.strftime("%I")) 
    minutes = int(time.strftime("%M")) 
    seconds = int(time.strftime("%S")) 
    
    analog_clock(hours, minutes, seconds) 

    window.update()  

    time.sleep(1) 

    pen.clear() 

window.mainloop() 
