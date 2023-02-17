import pandas as pd

data = pd.read_csv(r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day25-pandas-and-USStatesGame\us-states-game\50_states.csv")
print(data)

def get_state_cor(state):
    row = data[data.state == state]
    return (int(row.x), int(row.y))

all_states = data.state.to_list()

print(all_states)