from name_function import get_formatted_name

print("Enter 'q‘ at any time to quit.")
while True:
    first = input("\nPlease give me your first name: ")
    if first == 'q':
        break
    middle = input("\nPlease give me your middle name: ")
    if middle == 'q':
        break
    last = input("\nPlease give me your last name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last, middle)
    print(f"\nNearly formatted name:{formatted_name}")
