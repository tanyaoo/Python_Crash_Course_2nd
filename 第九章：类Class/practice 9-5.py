class User:
    """创建用户类"""
    def __init__(self, first_name, last_name, age):
        """初始化用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        """描述用户"""
        print(f"The user info is:\n-first_name:{self.first_name}\n-last_name:{self.last_name}\n-age:{self.age}\n")

    def greet_user(self):
        """问候用户"""
        name = self.first_name + self.last_name
        print(f"Hello,{name} ！！")

    def increment_login_attempts(self):
        """每次登录一次就将login_attempts的值加1"""
        self.login_attempts += 1

    def reset_login_attemps(self):
        """重置登录次数"""
        self.login_attempts = 0


tan_yao = User("tan", "yao", 30)
tan_yao.increment_login_attempts()      # 调用1次
tan_yao.increment_login_attempts()      # 调用第2次
tan_yao.increment_login_attempts()      # 调用第3次
print(tan_yao.login_attempts)

# 调用方法重置登录次数
print("重置登录次数")
tan_yao.reset_login_attemps()
print(tan_yao.login_attempts)



