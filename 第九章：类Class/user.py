class User:
    """创建用户类"""
    def __init__(self, first_name, last_name, age):
        """初始化用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """描述用户"""
        print(f"The user info is:\n-first_name:{self.first_name}\n-last_name:{self.last_name}\n-age:{self.age}\n")

    def greet_user(self):
        """问候用户"""
        name = self.first_name + self.last_name
        print(f"Hello,{name} ！！")

