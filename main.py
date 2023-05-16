import random
import turtle
import time

gamescreen = turtle.Screen()
gamescreen.bgcolor("light green")
gamescreen.title("Catch The Leo")

leo = turtle.Turtle()
leo.shape("turtle")
leo.shapesize(3)
leo.color("dark blue")
leo.speed(0)
leo.penup()

score = 0
start_time = 20

time_leo = turtle.Turtle()
time_leo.hideturtle()
time_leo.penup()
time_leo.goto(0, 300)
time_leo.write(f"Time: {start_time}", align="center", font=("Courier", 24, "normal"))

def timer():
    global start_time

    while start_time>0:
        time.sleep(1)
        start_time -= 1
        time_leo.clear()
        time_leo.write(f"Time: {start_time}", align="center", font=("Courier", 24, "normal"))



def leo_position():
    xy_pos_list = [*range(-200, 200)]
    global start_time

    while start_time > 0:
        x_pos = random.choice(xy_pos_list)
        y_pos = random.choice(xy_pos_list)
        leo.goto(x_pos, y_pos)
        time.sleep(0.7)




score_leo = turtle.Turtle()
score_leo.hideturtle()
score_leo.penup()
score_leo.goto(0, 260)
score_leo.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def scoring(x, y):
    global score
    score += 1
    score_leo.clear()
    score_leo.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

leo_position()
timer()
leo.onclick(scoring,btn=1)

turtle.done()
