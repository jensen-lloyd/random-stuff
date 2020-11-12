import random
import math
import turtle

print("Insert number of points:")
np = input()
while not np.isdigit():
        print("Insert number of points:")
        np = input()
np = int(np)

turtle.speed("fastest")
length = 600 # radius of circle and length of the square in pixels

#draw y axis
turtle.pensize(2)
turtle.forward(length + 40)
turtle.left(135)
turtle.forward(20)
turtle.back(20)
turtle.left(90)
turtle.forward(20)

turtle.penup()
turtle.home()
turtle.pendown()

#draw x axis
turtle.left(90)
turtle.forward(length + 40)
turtle.left(135)
turtle.forward(20)
turtle.back(20)
turtle.left(90)
turtle.forward(20)

turtle.penup()
turtle.goto(0,length)
turtle.left(45)
turtle.left(180)
turtle.pendown()

#draw quarter of circle
turtle.pencolor("red")
turtle.circle(length,-90)

inside = 0
for i in range(0,np):
        #get dot position
        x = random.uniform(0,length)
        y = random.uniform(0,length)
        d = math.sqrt(x**2 + y**2)
        if d <= length:
                inside += 1
                turtle.pencolor("red")
        else:
                turtle.pencolor("blue")
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.dot()

print("Inside of quarter-circle:")
print(inside)
print("Total amount of points:")
print(np)
print("Pi is approximately:")
print((inside / np) * 4.0)

turtle.exitonclick()
