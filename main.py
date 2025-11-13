import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_on = True

while game_on:
    answer_state = screen.textinput(title = "Guess the State", prompt = "What's another's state's name?")


turtle.mainloop()