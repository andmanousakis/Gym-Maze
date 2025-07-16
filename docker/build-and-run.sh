# File: docker/build-and-run.sh

#!/bin/bash

# Move to the directory where this script is located (i.e., docker/).
cd "$(dirname "$0")"

# Names defined in docker-compose.yml.
IMAGE_NAME="rl-agent:latest"
RL_CONTAINER_NAME="rl-agent"
TENSORBOARD_CONTAINER_NAME="tensorboard"

# Check if image exists.
image_exists=$(docker images -q $IMAGE_NAME)

# Check if the rl-agent container exists.
rl_container_exists=$(docker ps -a --format '{{.Names}}' | grep -w $RL_CONTAINER_NAME)

# Check if the tensorboard container exists.
tensorboard_container_exists=$(docker ps -a --format '{{.Names}}' | grep -w $TENSORBOARD_CONTAINER_NAME)

# Build images if they don't exist.
if [ -z "$image_exists" ]; then
  echo "Image '$IMAGE_NAME' not found. Building it..."
  docker compose build
else
  echo "Image '$IMAGE_NAME' already exists. Skipping build."
fi

# Start containers.
if [ -z "$rl_container_exists" ] || [ -z "$tensorboard_container_exists" ]; then
  echo "Starting containers..."
else
  echo "Containers already exist. Reusing them..."
fi

# Start services with docker-compose.
docker compose up
