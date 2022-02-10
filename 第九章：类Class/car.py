class Car:
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_describe_name(self):
        """返回整洁干净的描述性信息"""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """将里程表读数设置成特定值"""
        self.odometer_reading = mileage


my_new_car = Car("audi", "A8", 2022)
print(my_new_car.get_describe_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 90        # 修改odometer_reading的值
my_new_car.read_odometer()

print()

my_new_car.update_odometer(78)
my_new_car.read_odometer()
