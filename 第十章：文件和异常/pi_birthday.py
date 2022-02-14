file_name = "pi_digits.txt"

with open(file_name) as file_name:
    lines = file_name.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

your_birthday = input("Please enter you birthday,in the form mmddyy:")
if your_birthday in pi_string:
    print("your birthday appears in the first million digits of pi.")
else:
    print("your birthday does not appear in the first million digits of pi.")
