from stable_baselines3 import PPO
from env.api_maze_env import MazeAPIEnv
from stable_baselines3.common.monitor import Monitor
import time

# Generate a unique run name using timestamp.
timestamp = time.strftime("%Y%m%d_%H%M%S")
run_name = f"ppo_run_{timestamp}"

# Instantiate and wrap the custom environment.
env = MazeAPIEnv()
env = Monitor(env)

# Initialize the PPO model and log to the parent log directory.
model = PPO(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=2.5e-4,
    n_steps=128,
    batch_size=64,
    n_epochs=10,
    gamma=0.99,
    gae_lambda=0.95,
    clip_range=0.2,
    tensorboard_log="./tensorboard_logs/ppo"
)

# Train the PPO model and log under a unique subdirectory.
model.learn(total_timesteps=10000, tb_log_name=run_name)

# Save the trained model.
model.save(f"models/ppo_maze_{timestamp}")
