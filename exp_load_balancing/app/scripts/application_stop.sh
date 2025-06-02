#!/bin/bash
# Stop any existing application (e.g., a running Docker container)

CONTAINER_NAME="flask_app_container"

if [ "$(docker ps -q -f name=${CONTAINER_NAME})" ]; then
    echo "Stopping existing Docker container: ${CONTAINER_NAME}"
    docker stop ${CONTAINER_NAME}
    echo "Removing existing Docker container: ${CONTAINER_NAME}"
    docker rm ${CONTAINER_NAME}
fi

# Remove previous app files if necessary, but be careful not to remove essential deployment files
# For this example, we assume CodeDeploy handles cleanup of old files in the destination directory.
# If you have files outside the app directory that need cleanup, do it here.
echo "ApplicationStop hook executed."
