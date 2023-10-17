# 7.2 Write a program that prompts for a file name, then opens that file and
# reads through the file, looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines
# and compute the average of those values and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0  # Initialize a count for the lines
total = 0  # Initialize a total for the confidence values

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    # Extract the spam confidence value from the line
    colon_pos = line.find(':')
    confidence_str = line[colon_pos + 1:].strip()

    try:
        confidence = float(confidence_str)
        total += confidence
        count += 1
    except ValueError:
        print("Invalid confidence value found:", confidence_str)

if count > 0:
    average = total / count
    print("Average spam confidence:", average)
else:
    print("No spam confidence values found in the file.")

fh.close()
# This code will calculate the average spam confidence by counting the lines
# that start with "X-DSPAM-Confidence:" and extracting the floating-point values
# from those lines. It then calculates the average and prints it.
