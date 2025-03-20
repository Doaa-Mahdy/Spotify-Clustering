import pandas as pd
import subprocess
import sys
import os

# Use a raw string or replace \ with /
path = "/bd_a1"

def preprocess_data(input_file, output_file):
    """Perform data cleaning, transformation, reduction, and discretization."""
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return

        # Load dataset
        df = pd.read_csv(input_file)

        # Data Reduction: Select relevant columns
        selected_columns = [
            "danceability", "energy", "loudness", "mode",
            "speechiness", "acousticness", "instrumentalness",
            "liveness", "valence", "tempo"
        ]
        df = df[selected_columns]

        # Data Cleaning: Remove duplicates and missing values
        df = df.drop_duplicates().dropna()

        # Save preprocessed data
        df.to_csv(output_file, index=False)
        print(f"Preprocessed data saved to {output_file}")

        # Construct full path for eda.py
        eda_script = os.path.join(path, "eda.py")

        if not os.path.exists(eda_script):
            print(f"Error: EDA script '{eda_script}' not found.")
            return

        # Run eda.py with the preprocessed data file
        subprocess.run([sys.executable, eda_script, output_file], check=True)

    except Exception as e:
        print(f"Error during preprocessing: {e}")

if __name__ == "__main__":
    # Ensure script is run with an argument
    if len(sys.argv) < 2:
        print("Usage: python preprocess.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]  # Get input file from command line
    output_file = os.path.join(path, "res_dpre.csv")

    preprocess_data(input_file, output_file)
