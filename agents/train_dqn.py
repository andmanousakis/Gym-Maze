from stable_baselines3 import DQN
from env.api_maze_env import MazeAPIEnv
from stable_baselines3.common.monitor import Monitor
import time

# Unique run name based on timestamp.
timestamp = time.strftime("%Y%m%d_%H%M%S")
run_name = f"dqn_run_{timestamp}"

# Instantiate and wrap the environment.
env = MazeAPIEnv()
env = Monitor(env)

# Initialize the model, specifying the parent log directory.
model = DQN(
    "MlpPolicy",
    env,
    verbose=1,
    learning_rate=2.5e-4,
    buffer_size=100000,
    learning_starts=1000,
    batch_size=64,
    tau=1.0,
    gamma=0.99,
    train_freq=4,
    target_update_interval=1000,
    exploration_fraction=0.1,
    exploration_final_eps=0.05,
    tensorboard_log="./tensorboard_logs/dqn"
)

# Train the model; logs will go to ./tensorboard_logs/dqn/dqn_run_<timestamp>/
model.learn(total_timesteps=10000, tb_log_name=run_name)

# Save the model.
model.save(f"models/dqn_maze_{timestamp}")
