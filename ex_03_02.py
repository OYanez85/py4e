# Rewrite your pay program using try and except so that your program handles
# non-numeric input gracefully by printing a message and exiting the program.

sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
try:
        fh = float(sh)
        fr = float(sr)
except:
    print("Error, please enter numeric input")

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fh * fr
print("Pay:",xp)
