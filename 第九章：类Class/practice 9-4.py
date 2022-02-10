class Restaurant:
    """关于一家餐厅"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐厅的基本信息"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """餐厅描述"""
        print(f"The restaurant name is {self.restaurant_name},and the cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        """餐厅营业情况"""
        print("The restaurant is open !！")

    def set_number_served(self, set_number):
        """设置就餐人数"""
        self.number_served = set_number

    def increment_number_served(self, add_number):
        """将就餐人数递增"""
        self.number_served += add_number


my_restaurant = Restaurant("醉行湘西", "湘菜")
print(f"The restaurant has served {my_restaurant.number_served} people.")

# 修改number_served的值
my_restaurant.number_served = 10
print(f"The restaurant has served {my_restaurant.number_served} people.")

# 设置就餐人数
my_restaurant.set_number_served(20)
print(f"The restaurant has served {my_restaurant.number_served} people.")

# 增加就餐人数
my_restaurant.increment_number_served(90)
print(f"The restaurant has served {my_restaurant.number_served} people.")

