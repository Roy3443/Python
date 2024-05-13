# import colorgram
# rgb_colors=[]
# colours=colorgram.extract('image1.jpg', 30)
#
# for color in colours:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_colour= (r,g,b)
#     rgb_colors.append(new_colour)
# print(rgb_colors)
import turtle
import turtle as t
import random
tim=t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
t.colormode(255)
color_list=[ (236, 231, 233), (224, 233, 227), (207, 160, 82), (54, 88, 130), (145, 91, 40), (140, 26, 49), (221, 207, 105), (132, 177, 203), (158, 46, 83), (45, 55, 104), (169, 160, 39), (129, 189, 143), (83, 20, 44), (37, 43, 67), (186, 94, 107), (187, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 165), (194, 79, 73), (45, 74, 78), (80, 74, 44), (161, 201, 218), (57, 125, 121), (219, 175, 187), (169, 206, 172), (219, 182, 169)]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)
num_of_dots=100
for dot_count in range(1,num_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)
    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)









screen=t.Screen()
screen.exitonclick()