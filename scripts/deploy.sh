#!/bin/bash

echo "Building Docker image..."

docker build -t rock-paper-scissors .

echo "Running Docker container..."

docker run -it rock-paper-scissors
