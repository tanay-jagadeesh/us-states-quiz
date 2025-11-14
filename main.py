import turtle
import pandas

game_on = True

score = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")

while game_on:
    answer_state = screen.textinput(title = "Guess the State", prompt = "What's another's state's name?").title()
    correct_guess = data[data["state"] == answer_state]

    if not correct_guess.empty:
        score += 1
        print(f"{score}/50 states correct")
        turtle.penup()
        turtle.goto(correct_guess["x"].iloc[0], correct_guess["y"].iloc[0])
        turtle.write(correct_guess["state"].iloc[0])

        if score == 50:
            game_on = False




turtle.mainloop()

