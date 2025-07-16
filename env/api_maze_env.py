# File: env/api_maze_env.py

from dotenv import load_dotenv
load_dotenv()
import gymnasium as gym
from gym import spaces
import numpy as np
import requests
import os


# Read GRID_SIZE from .env (or fallback to 5).
GRID_SIZE = int(os.getenv("MAZE_GRID_SIZE", 5))

class MazeAPIEnv(gym.Env):

    """A custom Gymnasium environment that interacts with a maze API."""

    def __init__(self):

        # Initialize the superclass.
        super(MazeAPIEnv, self).__init__()

        # Base URL of the maze environment API.
        self.api_url = "http://maze-api:5005/api"

        # Define the action space: 4 discrete directions (0=up, 1=down, 2=left, 3=right).
        self.action_space = spaces.Discrete(4)

        # Define the observation space: 2D coordinates in a 5x5 grid.
        self.observation_space = spaces.Box(
            low=0, high=GRID_SIZE - 1, shape=(2,), dtype=np.int32
        )

        # Store the current state of the environment.
        self.state = None

    def reset(self, seed=None, options=None):

        """Reset the environment to its initial state."""

        # Call the API to reset the environment.
        res = requests.post(f"{self.api_url}/reset")

        # Extract the new state from the API response.
        self.state = np.array(res.json()['state'], dtype=np.int32)

        # Return the initial observation and info dict.
        return self.state

    def step(self, action):

        # API call.
        res = requests.post(f"{self.api_url}/step", json={'action': int(action)})
        data = res.json()

        self.state = np.array(data['next_state'], dtype=np.int32)
        terminated = data['done']
        raw_reward = data['reward']

        # Custom reward shaping (ignore the API reward if it's unhelpful)
        if terminated:
            if raw_reward >= 1:
                reward = 100  # goal reached
            else:
                reward = -10  # failed
        else:
            reward = -1  # time penalty

        return self.state, reward, terminated, {}

    def render(self):

        """Print the current position of the agent."""

        print(f"Current position: {self.state}")