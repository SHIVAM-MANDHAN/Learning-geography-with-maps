import time
from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.setup(800, 800)
screen.title("Name The State")
screen.bgpic("map_of_India.gif")


# def point(x, y):
#     print(x, y)
#
#
# screen.listen()
# screen.onclick(point)

tim = Turtle()
tim.hideturtle()
tim.penup()
tim.color("red")

try_again = Turtle()
try_again.hideturtle()
try_again.penup()
try_again.goto(180, 250)
# try_again.color("red")

high_score_file = open("high score")
high_score = int(high_score_file.read())
high_score_file.close()

h_score = Turtle()
h_score.speed("fastest")
h_score.hideturtle()
h_score.penup()
h_score.goto(-290, -300)
# h_score.color("brown")
h_score.write(arg=f"High Score : {high_score}", align='center', font=('Arial', 15, 'bold'))

file = pandas.read_csv("states.csv")

state_list = file["state"].to_list()

score = 0

game = True
while game:

    answer = screen.textinput(title=f"Your Score {score}/28", prompt="Name The State").title()

    if answer in state_list:
        state_row = file[file["state"] == answer]
        x_point = int(state_row["x"])
        y_point = int(state_row["y"])

        tim.goto(x_point, y_point)
        tim.write(arg=f"{answer}", align='center', font=('Arial', 10, 'bold'))
        score += 1

        if score > high_score:
            high_score = score
            high_score_file = open("high score", mode="w")
            high_score_file.write(str(high_score))
            high_score_file.close()
            h_score.clear()
            h_score.write(arg=f"High Score : {high_score}", align='center', font=('Arial', 15, 'bold'))

    elif answer == "Exit":
        game = False

    else:
        try_again.write(arg="Try Again...", align='center', font=('Arial', 40, 'normal'))
        time.sleep(1)
        try_again.clear()


