my_places = ["shanghai","xian","beijing"]
he_places = my_places[:]

my_places.append("hongkong")
he_places.append("taiwang")

places = [my_places,he_places]
for place in places:
    for itme in place:
        print(itme)
    print("______")
