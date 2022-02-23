import json

numbers = [1, 2, 3, 32, 4, 6]

filename = "numbers.json"
with open(filename, 'w') as f:
    json.dump(numbers, f)
    