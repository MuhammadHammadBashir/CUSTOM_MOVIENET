# Define the path to your .txt file with the URLs
input_file_path = "k600_train_path.txt"  # Replace with your file path
output_file_path = "activity_names.txt"

# Initialize a list to store the extracted activity names
activity_names = []

# Read from the .txt file and extract names
with open(input_file_path, 'r') as file:
    for line in file:
        line = line.strip()  # Remove any leading/trailing whitespace
        if "train/" in line and ".tar" in line:
            # Extract the part after 'train/' and before '.tar'
            activity_name = line.split("train/")[1].split(".tar")[0]
            activity_names.append(activity_name)

# Optionally, print the list of names
print(activity_names)

# Save the names line-by-line in an output file
with open(output_file_path, 'w') as file:
    for name in activity_names:
        file.write(name + "\n")

print(f"Activity names saved to {output_file_path}")
