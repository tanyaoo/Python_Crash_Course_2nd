def show_animals(file_animal):
    """展示文件中的动物名"""
    try:
        with open(file_animal) as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"文件{file_animal}不存在.")
        pass    #静默失败
    else:
        print(f"The File ({file_animal})`s Contents is:\n{contents}\n")


file_dogs = "dogs.txt"
file_cats = "cats.txt"


show_animals(file_cats)
show_animals(file_dogs)
