class Dog:
    """模拟狗类"""

    def __init__(self, name, age):
        """初始化狗类"""
        self.name = name
        self.age = age

    # @staticmethod
    def sit(self):
        """所有的狗都可以坐下"""
        print("the dog is sitting !!")

    # @staticmethod
    def roll(self):
        """所哟的狗都可以打滚"""
        print("the dog is rolling !!")


my_dog = Dog('fugui', 2)
print(my_dog.sit())
print(my_dog.roll())
print(my_dog.age)
print(f"my dog`s name is {my_dog.name},and it`s age is {my_dog.age}")



