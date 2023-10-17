# 3.1 Write a program to prompt the user for hours and rate per hour using input to 
# compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the
# hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of
# 10.50 per hour to test the program (the pay should be 498.75). You should use
# input to read a string and float() to convert the string to a number. Do not
# worry about error checking the user input - assume the user types numbers
# properly.

# Prompt the user for hours and rate per hour
hours_str = input("Enter hours worked: ")
rate_per_hour_str = input("Enter hourly rate: ")

# Convert the input strings to numbers (float)
hours = float(hours_str)
rate_per_hour = float(rate_per_hour_str)

# Calculate the gross pay
if hours <= 40:
    gross_pay = hours * rate_per_hour
    print(" ", gross_pay)
elif hours > 40:
    regular_hours = 40
    overtime_hours = hours - 40
    gross_pay = (regular_hours * rate_per_hour) + (overtime_hours * 1.5 * rate_per_hour)

# Print the calculated gross pay
print("", gross_pay)
