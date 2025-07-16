#!/bin/bash

# Navigate to script location.
cd "$(dirname "$0")"

echo "Stopping and removing containers..."
docker rm -f rl-agent tensorboard maze-api 2>/dev/null || echo "Containers not found."

echo "Removing Docker images..."
docker rmi -f rl-agent:latest 2>/dev/null || echo "Image 'rl-agent:latest' not found."
docker rmi -f tensorboard:latest 2>/dev/null || echo "Image 'tensorboard:latest' not found."
docker rmi -f tensorflow/tensorflow:2.13.0 2>/dev/null || echo "Image 'tensorflow/tensorflow:2.13.0' not found."
docker rmi -f docker-maze-api:latest 2>/dev/null || echo "Image 'docker-maze-api:latest' not found."

echo "Cleanup complete."
