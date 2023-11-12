#!/bin/bash

# Update package lists
sudo apt update

# Install Docker and answer 'Y' when prompted
sudo apt install -y docker.io

# Run the Docker container with the 'always' restart policy
sudo docker run -p 8443:8443 --restart always amiraniv/aws-polybot:v3.0
