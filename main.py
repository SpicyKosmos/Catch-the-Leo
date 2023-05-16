import random
import turtle
import time
import threading

gamescreen = turtle.Screen()
gamescreen.bgcolor("light green")
gamescreen.title("Catch The Leo")

leo = turtle.Turtle()
leo.shape("turtle")
leo.shapesize(3)
leo.color("blue")
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

    while start_time >= 0:
        time.sleep(1)
        start_time -= 1
        time_leo.clear()
        time_leo.write(f"Time: {start_time}", align="center", font=("Courier", 24, "normal"))
    gamescreen.clear()
    gamescreen.bgcolor("light Green")
    leo_over = turtle
    leo_over.hideturtle()
    leo_over.penup()
    leo_over.goto(0, 0)
    leo_over.write(f"Game Over\nYour Score: {score}", align="center", font=("Courier", 24, "normal"))

def leo_position():
    xy_pos_list = list(range(-200, 200))
    while start_time >= 0:
        x_pos = random.choice(xy_pos_list)
        y_pos = random.choice(xy_pos_list)
        leo.goto(x_pos, y_pos)
        time.sleep(0.6)

def scoring(x, y):
    global score
    score += 1
    score_leo.clear()
    score_leo.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))


score_leo = turtle.Turtle()
score_leo.hideturtle()
score_leo.penup()
score_leo.goto(0, 260)
score_leo.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

turtle.listen()
turtle.onkey(start_game, "s")  # "s" tuşuna basıldığında start_game fonksiyonunu çağır
turtle.onkey(exit_game, "e")  # "e" tuşuna basıldığında exit_game fonksiyonunu çağır
turtle.onkey(reset_game, "r")  # "r" tuşuna basıldığında reset_game fonksiyonunu çağır

leo.onclick(scoring)

timer_thread = threading.Thread(target=timer)
leo_position_thread = threading.Thread(target=leo_position)

timer_thread.start()
leo_position_thread.start()

gamescreen.mainloop()
