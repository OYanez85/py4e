# PARSING TEXT STRINGS
# 6.5 Write code using find() and string slicing (see section 6.10) to extract
# the number at the end of the line below. Convert the extracted value to a
# floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475 "

# Find the position of the colon in the string
colon_index = text.find(":")

if colon_index != -1:
    # Extract the substring after the colon
    number_str = text[colon_index + 1:].strip()  # Skip the ":" and strip whitespace

    try:
        # Convert the extracted substring to a float
        confidence = float(number_str)

        # Print the floating-point number
        print(confidence)
    except ValueError:
        print("Unable to convert to float")
else:
    print("Colon not found in the string")
