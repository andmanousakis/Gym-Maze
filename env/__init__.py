import os

# Ensure folders exist with correct permissions
os.makedirs("tensorboard_logs/dqn", exist_ok=True)
os.makedirs("models", exist_ok=True)