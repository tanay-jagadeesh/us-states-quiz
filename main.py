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

if data[data["state"] == answer_state]:
    print(data[data["x"]], data[data["y"]])
    print(f"{score}/50 states correct")









turtle.mainloop()

