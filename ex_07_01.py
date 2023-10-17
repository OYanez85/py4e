# 7.1 Write a program that prompts for a file name, then opens that file and
# reads through the file, and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# Prompt for a file name
file_name = input("Enter the file name: ")

try:
    # Open the file
    with open(file_name, 'r') as file:
        # Read the contents of the file and convert to uppercase
        file_contents = file.read().upper()

        # Remove trailing newlines to avoid double newlines in the output
        file_contents = file_contents.rstrip()

        # Print the contents in uppercase
        print(file_contents)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
