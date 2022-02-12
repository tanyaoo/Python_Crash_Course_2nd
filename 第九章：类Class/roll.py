from random import randint


class Die:
    """创建骰子"""
    def __init__(self, sides=6):
        """初始化属性"""
        self.sides = sides

    def roll_die(self):
        """打印随机数"""
        roll_number = randint(1, self.sides)
        return roll_number


# 创建一个骰子掷10次
my_Die = Die(20)
number_list = []
for a in range(10):
    number_list.append(my_Die.roll_die())
print(number_list)
