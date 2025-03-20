# README for Big Data Assignment 1 (data analysis pipline)

This document provides a step-by-step guide to executing the Big Data Assignment 1 project using Docker. The project involves setting up a Docker container with a specific environment, processing a dataset, and generating insights and visualizations.

## Prerequisites

- Docker installed on your local machine.
- A dataset file placed in the `bd-a1/` directory (we used spotify.csv).

## Project Structure

- `bd-a1/`
  - `Dockerfile`
  - `spotify.csv`
  - `load.py`
  - `dpre.py`
  - `eda.py`
  - `vis.py`
  - `model.py`
  - `final.sh`

## Step 1: Create the Directory and Place the Dataset

1. Create the `bd-a1/` directory on your local machine.
   ```sh
   mkdir -p bd-a1
2. Download and place your dataset in the bd-a1/ directory.
   ```sh
   cp /path/to/your/dataset.csv bd-a1/
## Step 2: Create the Dockerfile with specifications
include requirements Python packages: python3, pandas, numpy, seaborn, matplotlib, scikit-learn, scipy.
## Step 3: Build the image
docker build -t <image_name> 
## Step 4: Run docker container
docker run --name <container_name> <image_name>
## Step 5:create bash script to run the data analysis pipline
chmod +x final.sh
./final.sh
## Step 6: push to docker hub

docker login
docker push <username>/<image_name>
