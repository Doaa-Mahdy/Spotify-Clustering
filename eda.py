import pandas as pd
import subprocess
import os
import sys

# Define output directory
output_dir = "/bd_a1"


def exploratory_data_analysis(input_file):
    """Perform EDA and generate insights."""
    try:
        # Load the preprocessed dataset
        df = pd.read_csv(input_file)

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)

        # Check if required columns exist
        required_columns = ["danceability", "energy", "loudness", "valence", "tempo"]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            print(f"Error: Missing columns in dataset: {missing_columns}")
            return

        # List to store insights
        insights = []

        # Insight 1: Average Danceability and Energy
        avg_danceability = df["danceability"].mean()
        avg_energy = df["energy"].mean()
        insights.append(f"Insight 1: The average danceability of the dataset is {avg_danceability:.2f}, "
                        f"while the average energy is {avg_energy:.2f}.")

        # Insight 2: Correlation Between Loudness and Valence (Happiness)
        loudness_valence_corr = df["loudness"].corr(df["valence"])
        insights.append(f"Insight 2: The correlation between loudness and valence (happiness) is {loudness_valence_corr:.2f}, "
                        f"suggesting {'a positive' if loudness_valence_corr > 0 else 'a negative'} relationship.")

        # Insight 3: How Tempo Affects Danceability
        median_tempo = df["tempo"].median()
        slow_songs = df[df["tempo"] < median_tempo]
        fast_songs = df[df["tempo"] >= median_tempo]

        avg_danceability_slow = slow_songs["danceability"].mean()
        avg_danceability_fast = fast_songs["danceability"].mean()

        insights.append(f"Insight 3: Songs with a lower tempo (below {median_tempo:.2f} BPM) have an average danceability of "
                        f"{avg_danceability_slow:.2f}, while faster songs (above {median_tempo:.2f} BPM) have an average "
                        f"danceability of {avg_danceability_fast:.2f}. "
                        f"{'Faster songs tend to be more danceable.' if avg_danceability_fast > avg_danceability_slow else 'Slower songs tend to be more danceable.'}")

        # Save insights as text files in the output directory
        for i, insight in enumerate(insights, start=1):
            insight_file = os.path.join(output_dir, f"eda-in-{i}.txt")
            with open(insight_file, "w") as file:
                file.write(insight)

        print(f"EDA insights saved successfully in {output_dir}.")

        # Construct the path for vis.py
        vis_script = os.path.join(output_dir, "vis.py")

        if not os.path.exists(vis_script):
            print(f"Error: Visualization script '{vis_script}' not found.")
            return

        # Call vis.py and pass the processed file
        subprocess.run([sys.executable, vis_script, input_file], check=True)

    except Exception as e:
        print(f"Error during EDA: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python eda.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]  # Use the preprocessed dataset
    exploratory_data_analysis(input_file)
