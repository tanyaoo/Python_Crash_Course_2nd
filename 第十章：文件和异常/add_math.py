print("Please enter two number,we will add them and show the answer.")
while True:
    first_number = input("first number:")
    if first_number == "q":
        break
    second_number = input("second number:")
    if second_number == "q":
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Your enter is not number,please enter again.")
    else:
        print(f"the answer is {answer}.\n")
