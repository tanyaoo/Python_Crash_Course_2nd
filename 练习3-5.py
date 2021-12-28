friends = ['xiaolai','kobe','elon musk','hebe']

#kobe不能赴约
print(f"Because {friends[1]} was die,so cann`t for the dinner,I must invite another one.")

friends[1] = "jack ma"

print(friends)

for friend in friends:
    message = f"Dear {friend},I want to invite you to have a dinner tonight."
    print(message)
