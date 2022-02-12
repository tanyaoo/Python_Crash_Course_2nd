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


class IceCreamStand(Restaurant):
    """模拟冰淇淋"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化小店属性"""
        super().__init__(restaurant_name, cuisine_type)
        """继承"""
        self.flavors = ["pearl", "jasmine", "apple"]

    def display_flavors(self):
        """打印不同口味的冰淇淋"""
        for flavor in self.flavors:
            print(f"-{flavor}")


my_ice = IceCreamStand("guming", "naicha")
my_ice.display_flavors()
