from user import User


class Privileges:
    """权限类"""

    def __init__(self):
        """初始化属性"""
        self.privileges = ["can add post", "can delete post", "can ban user", "can add user"]

    def show_privileges(self):
        """展示管理权限"""
        for privilege in self.privileges:
            print(f"-{privilege}")


class Admin(User):
    """管理员"""

    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()


tan_yao = Admin("tan", "yao", 30)
tan_yao.privileges.show_privileges()