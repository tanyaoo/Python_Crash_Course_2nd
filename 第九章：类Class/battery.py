class Car:
    """模拟汽车"""

    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_describtive_name(self):
        """获取汽车的描述信息"""
        print(f"{self.make} {self.model} {self.year}")


class Battery:
    """模拟电池"""

    def __init__(self, battery_size=80):
        """初始化电池属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        # self.battery_size = new_battery_size
        print(f"This car has a {self.battery_size}-kwh battery.")

    def get_range(self):
        """根据电池容量指出续航里程"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 320

        print(f"This car can go {range} miles on a full charge.")


class ElectricCar(Car):
    """模拟电动汽车，继承汽车的所有属性，并添加特殊属性"""

    def __init__(self, make, model, year):
        """初始化属性"""
        super().__init__(make, model, year)
        """继承父类属性"""
        self.battery = Battery(100)


my_tesla = ElectricCar('audi', 'a4', 2022)
my_tesla.get_describtive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
