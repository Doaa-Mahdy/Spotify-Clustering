import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import subprocess
import os
import sys

# Define base path
path = "/bd_a1"

def create_visualization(input_file, output_image):
    """Generate a heatmap of correlations between audio features."""
    try:
        # Load the preprocessed dataset
        df = pd.read_csv(input_file)

        # Select relevant features for correlation
        features = ["danceability", "energy", "loudness", "speechiness", 
                    "acousticness", "instrumentalness", "liveness", "valence", "tempo"]
        
        # Compute correlation matrix
        correlation_matrix = df[features].corr()

        # Create heatmap
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)

        # Title
        plt.title("Correlation Heatmap of Spotify Audio Features")

        # Save visualization
        plt.savefig(output_image, dpi=300, bbox_inches="tight")
        print(f"Visualization saved as {output_image}")

        # Call model.py if it exists
        model_script = os.path.join(path, "model.py")
        if os.path.exists(model_script):
            subprocess.run(["python", model_script, input_file])
        else:
            print(f"Error: '{model_script}' not found.")

    except Exception as e:
        print(f"Error during visualization: {e}")

if __name__ == "__main__":
    input_file = sys.argv[1]   # Use preprocessed data
    output_image = os.path.join(path, "vis.png")
    create_visualization(input_file, output_image)
