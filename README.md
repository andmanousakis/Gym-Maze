# Maze Navigation using Reinforcement Learning

This project demonstrates the implementation and training of Reinforcement Learning (RL) agents to solve a 5x5 maze navigation task. It uses a remote API-based Gym environment wrapped with Gymnasium, and two popular RL algorithms: Deep Q-Network (DQN) and Proximal Policy Optimization (PPO).

## Project Setup

### Installation

From parent directory run the following commands

Build the environment and install dependencies:
```bash
make build
```

### Training Agents

Train the DQN agent:
```bash
make train-dqn
```

Train the PPO agent:
```bash
make train-ppo
```

### Evaluation

Evaluate the trained agents:
```bash
make evaluate
```

### Visualizing Training Metrics

Open TensorBoard at:
```
http://localhost:6006/
```

### Cleanup

To clean generated files and reset the environment:
```bash
make clean