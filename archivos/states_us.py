import pandas as pd
import turtle  


screen = turtle.Screen()
screen.title("U.S States Game")
image = "archivos//US_states.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
#screen.exitonclick()

data = pd.read_csv("archivos//states_xy.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) <= 3:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/4 Guess the State", 
                                    prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)


screen.exitonclick()