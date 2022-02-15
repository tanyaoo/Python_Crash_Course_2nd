
while True:
    name = input("please enter you full name:")
    print(f"Welcome,{name}")
    if name == "q":
        break

    name_file = "guest.txt"
    with open(name_file, 'a') as file_object:
        file_object.write(f"{name}\n")
