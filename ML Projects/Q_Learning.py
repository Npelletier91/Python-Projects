import numpy as np

# Environment setup, grid maze where 0s are empty cells and 1s are obsticals and 2 is the goal
grid = np.array([
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0],
    [0, 0, 0, 0, 2]
])
num_rows, num_cols = grid.shape
state_size = num_rows * num_cols # 5 x 5 = 25 different cells/state that the agent can be in
action_size = 4  # Up, Down, Left, Right = 4 possible actions

# Hyperparameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
total_episodes = 1000  # Total episodes for training

# Q-table - 2D grid of zeros in shape of 25(all states) x 4(all actions)
q_table = np.zeros((state_size, action_size))

# Convert a grid position to a state number
def pos_to_state(row, col):
    return row * num_cols + col

# Choose an action using based on the highest Q-value 
def choose_action(state):
    if np.random.rand() < epsilon: # sometimes choose a random action not according to highest Q-value
        return np.random.randint(action_size)
    else:
        return np.argmax(q_table[state]) # highest Q-value from the state the agent is standing on


# The step function to move the agent
def step(state, action):
    row, col = divmod(state, num_cols) # convering state to a grid position, find the index of state(where agent is)
    if action == 0 and row > 0:  # Up
        row -= 1
    elif action == 1 and row < num_rows - 1:  # Down
        row += 1
    elif action == 2 and col > 0:  # Left
        col -= 1
    elif action == 3 and col < num_cols - 1:  # Right
        col += 1
    new_state = pos_to_state(row, col)
    reward = -1  # Default reward
    done = False
    if grid[row][col] == 2:  # Check if goal is reached
        reward = 100
        done = True
    elif grid[row][col] == 1:  # Check if it's an obstacle
        reward = -100
        done = True
    return new_state, reward, done

# Training the agent
for episode in range(total_episodes): # iterate 1000 times
    state = np.random.randint(state_size)  # Start at a random state(position) each time
    done = False

    
    while not done: # while the agent has NOT reached an obstacle or goal
        action = choose_action(state) # move up, down, right, or left from the current randomly choosen state(position)
        new_state, reward, done = step(state, action) # take action and step in the choosen direction
        # Update Q-table with values based on the reward from the action taken.
        q_table[state, action] = q_table[state, action] + alpha * (reward + gamma * np.max(q_table[new_state]) - q_table[state, action])
        state = new_state

# change values to remove scientific notation when printing
np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.2f}'.format})

# for printing action on each state
actions = ["Up", "Down", "Left", "Right"]


print("Trained Q-table:")
for state, values in enumerate(q_table):
    best_action_index = np.argmax(values) # highest value = best action
    best_action = actions[best_action_index] # from actions array
    print(f"State {state}: {np.around(values, 2)} - Best action: {best_action}")