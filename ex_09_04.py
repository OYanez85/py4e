# 9.4 Write a program to read through the mbox-short.txt and figure out who has
#  sent the greatest number of mail messages. The program looks for 'From ' lines
#  and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to
# a count of the number of times they appear in the file. After the dictionary
# is produced, the program reads through the dictionary using a maximum loop to
# find the most prolific committer.

# Create an empty dictionary to store sender counts
sender_counts = {}

# Open the mbox-short.txt file
with open("mbox-short.txt", "r") as file:
    for line in file:
        # Check if the line starts with 'From '
        if line.startswith("From "):
            # Split the line into words and get the sender's email address (second word)
            words = line.split()
            sender = words[1]

            # Update the sender's count in the dictionary
            sender_counts[sender] = sender_counts.get(sender, 0) + 1

# Find the sender with the highest count
most_prolific_sender = None
most_prolific_count = None

for sender, count in sender_counts.items():
    if most_prolific_sender is None or count > most_prolific_count:
        most_prolific_sender = sender
        most_prolific_count = count

# Print the most prolific sender and their message count
print(most_prolific_sender, most_prolific_count)
