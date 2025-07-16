# File: api/main.py

import os
import random
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Simple Maze state and logic (5x5 grid).
current_state = [0, 0]  # starting position

# Define action schema.
class Action(BaseModel):
    action: int  # 0=up, 1=down, 2=left, 3=right

# Maze boundaries.
GRID_SIZE = int(os.getenv("MAZE_GRID_SIZE", 5))

@app.post("/api/reset")
def reset():
    global current_state

    # 🎲 Randomize start, but not at the goal
    while True:
        current_state = [
            random.randint(0, GRID_SIZE - 1),
            random.randint(0, GRID_SIZE - 1)
        ]
        if current_state != [GRID_SIZE - 1, GRID_SIZE - 1]:
            break

    return {"state": current_state}

@app.post("/api/step")
def step(action: Action):
    global current_state
    x, y = current_state
    if action.action == 0 and y > 0:
        y -= 1
    elif action.action == 1 and y < GRID_SIZE - 1:
        y += 1
    elif action.action == 2 and x > 0:
        x -= 1
    elif action.action == 3 and x < GRID_SIZE - 1:
        x += 1

    current_state = [x, y]

    # Simple reward logic: reward = 1 if at bottom-right, else 0
    done = (x == GRID_SIZE - 1 and y == GRID_SIZE - 1)
    reward = 1 if done else 0

    return {
        "next_state": current_state,
        "reward": reward,
        "done": done
    }
