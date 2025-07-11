import time
import random
import turtle
width,height=500,600
colors=['red','green','blue','yellow','black','orange','purple','pink','brown','gray']
def get_number_of_racers():
    racers=0
    while True:
        racers=input("enter the number of racers(2-10):")
        if racers.isdigit():
            racers=int(racers)
            if 2<=racers<=10:
                return racers
            else:
                print('number not in range 2-10. try again')
        else:
            print('input is not numeric.. try again')
            continue
def race(colors):
    turtles=create_turtle(colors)
    while True:
         for racer in turtles:
             distance= random.randrange(1,20)
             racer.forward(distance)

             x,y=racer.pos()
             if y>=height//2-10:
                 return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles=[]
    spacingx=width//(len(colors)+1)
    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-width//2+(i+1)*spacingx,-height//2+20)
        racer.pendown()
        turtles.append(racer)
    return turtles  
def init_turtle():
    screen=turtle.Screen()
    screen.setup(width,height)
    screen.title('turtle racing')

racers=get_number_of_racers()
init_turtle()
random.shuffle(colors)
colors=colors[:racers]

winner=race(colors)
print("the wiiner is the turtle with colour:",winner)
time.sleep(5)