# File: evaluation/evaluate_agents.py

import os
from stable_baselines3 import DQN, PPO
from stable_baselines3.common.monitor import Monitor
from stable_baselines3.common.evaluation import evaluate_policy
from env.api_maze_env import MazeAPIEnv

# Define trained model paths (update filenames as needed).
models = {
    "DQN": "models/dqn_maze_20250715_230615",
    "PPO": "models/ppo_maze_20250715_230735"
}

for algo, model_path in models.items():
    print(f"\nEvaluating {algo}...")

    if not os.path.isfile(model_path + ".zip"):
        print(f"Skipping {algo}: Model file not found at {model_path}.zip")
        continue

    try:
        # Load model.
        model = DQN.load(model_path) if algo == "DQN" else PPO.load(model_path)

        # Use Monitor for consistent logging.
        env = Monitor(MazeAPIEnv())

        # Evaluate over 100 episodes.
        mean_reward, std_reward = evaluate_policy(
            model,
            env,
            n_eval_episodes=100,
            deterministic=True,
            render=False
        )

        print(f"{algo}: Mean reward = {mean_reward:.2f} ± {std_reward:.2f}")

    except Exception as e:
        print(f"Error evaluating {algo}: {e}")
