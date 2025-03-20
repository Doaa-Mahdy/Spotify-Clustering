#!/bin/bash

# Define container ID and destination folder
CONTAINER_ID="eeb3757172e8"
DESTINATION="C:\Everything\NU\Year3-Semester2\Big Data\Assign1\bd-a1\service-result"

# Ensure destination directory exists
mkdir -p "$DESTINATION"

# Copy output files from container to local machine
docker cp "$CONTAINER_ID:/bd_a1/res_dpre.csv" "$DESTINATION"
docker cp "$CONTAINER_ID:/bd_a1/eda-in-1.txt" "$DESTINATION"
docker cp "$CONTAINER_ID:/bd_a1/eda-in-2.txt" "$DESTINATION"
docker cp "$CONTAINER_ID:/bd_a1/eda-in-3.txt" "$DESTINATION"
docker cp "$CONTAINER_ID:/bd_a1/vis.png" "$DESTINATION"
docker cp "$CONTAINER_ID:/bd_a1/k.txt" "$DESTINATION"

echo "Files copied successfully to $DESTINATION"

# Stop the container
docker stop "$CONTAINER_ID"

echo "Container $CONTAINER_ID stopped."
