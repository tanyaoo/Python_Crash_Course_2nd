from car import Car


class ElectricCar(Car):     # 一定要在子类名称后面把父类括起，指出父类的名称
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类属性
        再初始化电动汽车的特有属性
        """
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """描述电池容量"""
        print(f"The electric car has a {self.battery_size}-kwh battery.")


my_tesla = ElectricCar("Tesla", "model s", 2022)
print(my_tesla.get_describe_name())
my_tesla.describe_battery()
