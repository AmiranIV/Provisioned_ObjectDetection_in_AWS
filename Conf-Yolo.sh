#!/bin/bash

# Update package lists
sudo apt update

# Install Docker and answer 'Y' when prompted
sudo apt install -y docker.io

# Run the Docker container with the 'always' restart policy
sudo docker run --restart always amiraniv/aws-yolov5:v1.0
