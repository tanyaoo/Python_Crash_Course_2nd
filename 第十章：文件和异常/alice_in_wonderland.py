file_name = 'alice in wonderland.txt'

try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print("The file is not exist.")
else:
    words = contents.split()
    number_word = len(words)
    print(f"The file {file_name} has about {number_word} words.")
