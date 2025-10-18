#Task 1: Read a File and Handle Errors 

# Python program to read and print contents of a file line by line
# and handle error if the file does not exist.

try:
    # Try to open the file in read mode
    with open("sample.txt", "r") as file:
        print("File exists, Reading content:\n")
        # Read and print each line
        for line in file:
            print(line.strip())
except FileNotFoundError:
    # Handle the case where the file is missing
    print("The file 'sample.txt' was not found.")



#Task 2: Write and Append Data to a File

# Python program to write, append, and read from a file

# Step 1: Take user input and write it to output.txt
text = input("Enter text to write to the file: ")

# Write mode - creates or overwrites the file
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt.\n")

# Step 2: Take additional input and append it to the same file
additional_text = input("Enter additional text to append: ")

# Append mode - adds data without removing existing content
with open("output.txt", "a") as file:
    file.write(additional_text + "\n")
print("Data successfully appended.\n")

# Step 3: Read and display the final content
print("Final content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
