file_name = "programming.txt"

names = 'tanyao'
with open(file_name, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    file_object.write(names)
