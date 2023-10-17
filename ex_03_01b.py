# 3.1 Write a program to prompt the user for hours and rate per hour using input
# to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times
# the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate
# of 10.50 per hour to test the program (the pay should be 498.75). You should
# use input to read a string and float() to convert the string to a number. Do
# not worry about error checking the user input - assume the user types numbers
# properly

python hours_worked = None
hourly_rate = None
total_pay = 0.0
done = False
while not done:
    hours_worked = input("Enter the number of hours worked: ")
    if hours_worked == "done":
        done = True
        break
    else: if float(hours_worked) > 40:
        total_pay += (float(hourly_rate) * 40) total_pay += (float(hourly_rate) * 1.5) * (float(hours_worked) - 40)
        else: total_pay += (float(hourly_rate) * hours_worked) hourly_rate = input("Enter the hourly rate: ")
    if hourly_rate == "done": done = True
        break
    else: hourly_rate = float(hourly_rate)
    print(f"Total pay: ${total_pay:.2f}")
