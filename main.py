import turtle
import pandas

# Game setup
game_on = True
total = []  # List to track guessed states and prevent duplicates
score = 0

# Screen setup
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

# Set the main turtle to display the map image
turtle.shape(image)

# Load state data from CSV (contains state names and x, y coordinates)
data = pandas.read_csv("50_states.csv")

# Create a separate turtle for writing state names on the map
writer = turtle.Turtle()
writer.hideturtle()  # Hide the turtle shape
writer.penup()  # Prevent drawing lines when moving

# Main game loop
while game_on:
    # Get user input and convert to title case
    answer_state = screen.textinput(title = f"{score}/50 states correct Guess the State", prompt = "What's another's state's name?").title()
    # Filter data to find matching state
    correct_guess = data[data["state"] == answer_state]

    # Check if state hasn't been guessed before
    if answer_state not in total:
        # Check if state exists in the data (if you found a matching row then do this)
        if not correct_guess.empty:
            score += 1
            # Move writer to state's coordinates and write the name
            writer.goto(correct_guess["x"].iloc[0], correct_guess["y"].iloc[0])
            writer.write(correct_guess["state"].iloc[0])
            # Add to list of guessed states
            total.append(answer_state)
            # Check if all 50 states have been guessed
            if score == 50:
                game_on = False




turtle.mainloop()

