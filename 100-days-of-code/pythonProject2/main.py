import turtle as t
import random
tim=t.Turtle()
t.colormode(255)

# def draw(num_of_sides):
#     angle = 360 / num_of_sides
#     for _ in range(num_of_sides):
#         tim.forward(100)
#         tim.right(angle)
# for shape_side_n in range(3,11):
#     draw(shape_side_n)
def random_colour():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colour=(r,g,b)
    return colour

tim.speed("fastest")
def draw_spiro(size_of_gap):

    for _ in range(int(360/size_of_gap)):
         tim.color(random_colour())
         tim.circle(100)
         tim.setheading(tim.heading()+size_of_gap)

draw_spiro(7)

screen=t.Screen()
screen.exitonclick()



































screen=Screen()
screen.exitonclick()