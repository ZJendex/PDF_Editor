import os
import pandas as pd
from datetime import datetime

# Function to extract data from the text file
def extract_data(file_path):
    subject_data = {
        "Height": None,
        "Weight": None,
        "Age": None,
        "Gender": None
    }

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            if "Height" in line:
                subject_data["Height"] = float(line.split(":")[1].strip())
            elif "Weight" in line:
                subject_data["Weight"] = float(line.split(":")[1].strip())
            elif "Age" in line:
                subject_data["Age"] = int(line.split(":")[1].strip())
            elif "Gender" in line:
                subject_data["Gender"] = line.split(":")[1].strip()

    return subject_data

# Path to the directory where text files are stored
directory_path = "G:\My Drive\\2-PolyPulse\Docs\subject_basic_data"  # Replace this with the directory you want to scan

# Prepare a list to hold the data
data_list = []

index = 1
# Iterate through files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):  # Check if the file is a text file
        file_path = os.path.join(directory_path, filename)
        
        # Extract subject data
        subject_data = extract_data(file_path)

        # Get the file's modification date
        date_modified_timestamp = os.path.getmtime(file_path)
        date_modified = datetime.utcfromtimestamp(date_modified_timestamp).strftime('%m/%d/%Y')

        # Extract the subject ID from the filename (before the first period)
        subject_id = index  # Get the subject ID (everything before the first dot)
        index += 1
        
        # Prepare the row for this subject
        data_row = [
            subject_id,
            date_modified,
            subject_data["Weight"],
            subject_data["Height"],
            subject_data["Age"],
            subject_data["Gender"]
        ]
        data_list.append(data_row)

# Create a DataFrame from the collected data
df = pd.DataFrame(data_list, columns=["Subject ID", "Date Modified", "Weight", "Height", "Age", "Gender"])

df["Date Modified"] = pd.to_datetime(df["Date Modified"], format='%m/%d/%Y')

# Sort the DataFrame by "Date Modified"
df = df.sort_values(by="Date Modified", ascending=True)

# Save the result to a CSV file
output_file = "subject_data.csv"
df.to_csv(output_file, index=False)