# Variable
fname = input("Enter file name: ")

# Open file
fhand = open(fname)

# Creating a list to store unique words
unique_words = []

# Read the file line by line and split words
for line in fhand:
    words = line.split()
    for word in words:
        # Check if the word is not in the list, then append it
        if word not in unique_words:
            unique_words.append(word)

# Sort the list of unique words
unique_words.sort()

# Print the list
for word in unique_words:
    print(word)
