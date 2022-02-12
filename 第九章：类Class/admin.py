from user import User


class Admin(User):
    """管理员"""

    def __init__(self, first_name, last_name, age):
        """初始化属性"""
        super().__init__(first_name, last_name, age)
        """继承"""
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_pivileges(self):
        """展示管理员权限"""

        for privilege in self.privileges:
            print(f"-{privilege}")


# 创建名为“tanyao”的管理员实例
tanyao = Admin("tan", "yao", 30)
print(f"管理员{tanyao.first_name + tanyao.last_name}的权限如下：")
tanyao.show_pivileges()
