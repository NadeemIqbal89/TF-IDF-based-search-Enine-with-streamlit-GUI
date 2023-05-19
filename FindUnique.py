import pandas as pd
import csv

# Read input CSV file
input_file_path = "AllLematizeNews.csv"
output_file_path = "UniqueWord.csv"

# Load CSV data into a pandas DataFrame
df = pd.read_csv(input_file_path, encoding="ISO-8859-1")

# Extract unique words from the DataFrame
unique_words = set()
for index, row in df.iterrows():
    words = row[4].split() # Assumes 'text' is the column name in your CSV containing the text to be processed
    unique_words.update(words)

# Convert set of unique words to list
unique_words_list = list(unique_words)

# Write the unique words to the output CSV file
with open(output_file_path, 'w', encoding="ISO-8859-1") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['unique_words']) # Write header
    writer.writerows(zip(unique_words_list)) # Write unique words to rows