import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# to get the position of each state by clicking on them:
# these x and ys go to 50_states.csv file
# def get_position(x, y):
#     print(x, y)


# turtle.onscreenclick(get_position)
guessed_states = []
missed_states = []
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
while len(guessed_states) < 50:
    # creat a pop up box
    state_name = screen.textinput(title=f"{len(guessed_states)}/50", prompt="Please insert a state's name").title()
    # if the user inserted a state's name that was among 50 states, write it on the correct position on the map
    if state_name == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missed_states.append(state)
        missing = pandas.DataFrame(missed_states)
        missing.to_csv("to_learn.csv")
        break
    if state_name in all_states:
        guessed_states.append(state_name)
        inserted_state = data[data.state == state_name]
        print(inserted_state)
        writer = turtle.Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(int(inserted_state.x), int(inserted_state.y))
        writer.write(state_name)

# to keep the screen open after each click we should use mainloop() function instead of exitonclick()
# turtle.mainloop()

