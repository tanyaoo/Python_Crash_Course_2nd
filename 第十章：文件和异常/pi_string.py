file_name = "pi_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:9]}...")
print(len(pi_string))
