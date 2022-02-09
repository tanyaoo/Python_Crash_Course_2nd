class Restaurant:
    """关于一家餐厅"""

    def __init__(self, restaurant_name, cuisine_type):
        """餐厅的基本信息"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """餐厅描述"""
        print(f"The restaurant name is {self.restaurant_name},and the cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        """餐厅营业情况"""
        print("The restaurant is open !！")


my_restaurant = Restaurant("'向家村面条'", "'面条'")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
