friends = ['xiaolai','kobe','elon musk','hebe']

#kobe不能赴约
print(f"Because {friends[1]} was die,so cann`t for the dinner,I must invite another one.")

friends[1] = "jack ma"

print("我找到一张更大的餐桌，可以多邀请三个好朋友")

#邀请好朋友“Huateng Ma”、"tanyao"、"cml"
friends.insert(0,"Huateng Ma")
friends.insert(2,"tanyao")
friends.append("cml")

print(friends)

for friend in friends:
    message = f"Dear {friend},I want to invite you to have a dinner tonight."
    print(message)
