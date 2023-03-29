import argparse
import pandas as pd

# Define command line arguments
parser = argparse.ArgumentParser(description="Remove a column from a CSV file.")
parser.add_argument("input_file", type=str, help="Path to input CSV file")
parser.add_argument("output_file", type=str, help="Path to output CSV file")
parser.add_argument("column_index", type=int, help="Index of column to remove (starting at 0)")

# Parse command line arguments
args = parser.parse_args()

# Read input file into a pandas dataframe
df = pd.read_csv(args.input_file)

# Remove the specified column
df = df.drop(df.columns[args.column_index], axis=1)

# Write the modified dataframe to the output file
df.to_csv(args.output_file, index=False)
