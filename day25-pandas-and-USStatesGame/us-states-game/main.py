IMAGE = r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-pandas-and-USStatesGame\us-states-game\blank_states_img.gif"

import turtle
import data
import pandas

screen = turtle.Screen()
screen.title("U.S States Game!")

screen.addshape(IMAGE)
turtle.shape(IMAGE)


writer = turtle.Turtle()
writer.ht()
writer.pu()



guesses_states = []

while len(guesses_states) < 50:
    answer_state = screen.textinput(title=f"{len(guesses_states)}/50 States Correct", prompt="What's another state's name?").title()
    
    if answer_state == "Exit":
        states_to_learn = [state for state in data.all_states if state not in guesses_states]
        
        pandas.DataFrame(states_to_learn).to_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-pandas-and-USStatesGame\us-states-game\states_to_learn.csv")
        break
    
    if answer_state in data.all_states:
        guesses_states.append(answer_state)
        writer.goto(data.get_state_cor(answer_state))
        writer.write(f"{answer_state}")
