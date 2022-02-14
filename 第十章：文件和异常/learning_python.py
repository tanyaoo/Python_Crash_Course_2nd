file_name = "python_knowlege.txt"

# with open(file_name) as file_object:
#     contents = file_object.read()
#     print(contents, end="\n\n")
#     for line in contents:
#         print(line)

with open(file_name) as file_object_2:
    lines = file_object_2.readlines()
    print(lines)
for line in lines:
    print(line.replace("python", "java"))


