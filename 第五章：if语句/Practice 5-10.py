current_users = ['tanyao','Cml','admin','Musk','navl']
new_users = ['tanyao','cml','kobe','olyer','curry']

users = []
for current_user in current_users:
    users.append(current_user.lower())
# print(users)

for new_user in new_users:
    if new_user in users:
        print(f'用户名{new_user}已被占用。')
    else:
        print(f'你可以使用此用户名{new_user}。')
