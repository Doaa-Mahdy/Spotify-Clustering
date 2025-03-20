import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import os
import sys

# Define base path
path = "/bd_a1"

def apply_kmeans(input_file, output_file, k=3):
    """Apply K-means clustering on selected features and save cluster sizes."""
    try:
        # Load the preprocessed dataset
        df = pd.read_csv(input_file)

        # Select numerical features suitable for clustering
        features = ["danceability", "energy", "loudness", "speechiness", 
                    "acousticness", "instrumentalness", "liveness", "valence", "tempo"]

        # Normalize features using Min-Max scaling
        scaler = MinMaxScaler()
        df_scaled = pd.DataFrame(scaler.fit_transform(df[features]), columns=features)

        # Apply K-means clustering
        kmeans = KMeans(n_clusters=k, random_state=42, n_init="auto")  # Adjust for newer sklearn versions
        df["cluster"] = kmeans.fit_predict(df_scaled)

        # Count number of records in each cluster
        cluster_counts = df["cluster"].value_counts().sort_index()

        # Save cluster counts to a text file
        with open(output_file, "w") as file:
            for cluster, count in cluster_counts.items():
                file.write(f"Cluster {cluster}: {count} records\n")

        print(f"Cluster sizes saved to {output_file}")

    except Exception as e:
        print(f"Error during K-means clustering: {e}")

if __name__ == "__main__":
    input_file = sys.argv[1]   # Use preprocessed data
    output_file = os.path.join(path, "k.txt")
    apply_kmeans(input_file, output_file)
