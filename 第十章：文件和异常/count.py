filename = "alice in wonderland.txt"

with open(filename, encoding="utf-8") as f:
    contents = f.read()
    words = contents.lower().split()
    print(words)
    print(contents.count('ebook'))
