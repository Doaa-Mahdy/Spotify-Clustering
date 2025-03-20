import pandas as pd
import subprocess
import os
import sys

# Define base path
path = "/bd_a1"

def load_data(file_path, output_file):
    """Load the Spotify dataset from a CSV file and save it for preprocessing."""
    try:
        # Check if the input file exists
        if not os.path.exists(file_path):
            print(f"Error: The file '{file_path}' does not exist.")
            return

        df = pd.read_csv(file_path)
        print("Dataset loaded successfully!")

        # Save the loaded dataset
        df.to_csv(output_file, index=False)
        print(f"Dataset saved to {output_file}.")

        # Construct path for dpre.py
        dpre_script = os.path.join(path, "dpre.py")

        # Check if dpre.py exists before calling it
        if not os.path.exists(dpre_script):
            print(f"Error: Preprocessing script '{dpre_script}' not found.")
            return

        # Call dpre.py and pass the processed file
        subprocess.run([sys.executable, dpre_script, output_file], check=True)

    except Exception as e:
        print(f"Error loading dataset: {e}")

if __name__ == "__main__":
    input_file = os.path.join(path, "spotify.csv")
    output_file = os.path.join(path, "res_dpre.csv")
    load_data(input_file, output_file)
