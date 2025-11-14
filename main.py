import turtle
import pandas

score = 0
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title = "Guess the State", prompt = "What's another's state's name?").title()

data = pandas.read_csv("50_states.csv")

correct_guess = data[data["state"] == answer_state]










turtle.mainloop()

