file_name = "alice.txt"

try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("Sorry,the file is not exist.")
else:
    print(contents)
