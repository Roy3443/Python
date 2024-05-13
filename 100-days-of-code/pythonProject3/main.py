import turtle
from turtle import Turtle,Screen
import random

is_race_on=False
screen=Screen()
colours=["red","orange","yellow","green","blue","pink"]
all_turtles=[]

screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt="Which turtle do u think will win and enter colour")
y_pos=[-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            turtle.setheading(180)
            turtle.forward(rand_dist)
        if turtle.xcor()<-230:
            is_race_on = False
            win_color = turtle.pencolor()
            if win_color==user_bet:
                print(f"Youve won The {win_color} turtle is the winner")
            else:
                print(f"Youve lost The {win_color} turtle is the winner")
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)









screen.exitonclick()
