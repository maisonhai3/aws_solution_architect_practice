#!/bin/bash
# Install dependencies, pre-warm cache, etc.

APP_DIR="/home/ec2-user/app"

echo "BeforeInstall hook started."

# Ensure the app directory exists
if [ ! -d "$APP_DIR" ]; then
    echo "Creating application directory: $APP_DIR"
    mkdir -p "$APP_DIR"
fi

# Navigate to the app directory (or where your Dockerfile and app code will be)
cd "$APP_DIR" || exit 1

echo "Logging in to Amazon ECR..."
# The ECR login command will be specific to your AWS region and account ID.
# This should ideally be done by the EC2 instance role having ECR pull permissions.
# Example for us-east-1, replace 123456789012 with your AWS Account ID
# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.us-east-1.amazonaws.com
# For this script, we assume the instance role is configured and docker can pull from ECR without explicit login here.

# Pull the image details from imageDetail.json (created by GitHub Actions)
if [ -f "imageDetail.json" ]; then
    IMAGE_URI=$(jq -r '.ImageURI' imageDetail.json)
    if [ -n "$IMAGE_URI" ]; then
        echo "Pulling Docker image: $IMAGE_URI"
        docker pull "$IMAGE_URI"
        if [ $? -ne 0 ]; then
            echo "Failed to pull Docker image: $IMAGE_URI" >&2
            exit 1
        fi
        echo "Docker image pulled successfully."
    else
        echo "ImageURI not found in imageDetail.json" >&2
        exit 1
    fi
else
    echo "imageDetail.json not found. This file is expected to be part of the deployment bundle and contain the ECR image URI." >&2
    # exit 1 # You might want to exit if this file is critical for your deployment strategy
fi

echo "BeforeInstall hook completed."
