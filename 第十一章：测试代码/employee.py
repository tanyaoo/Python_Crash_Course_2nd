class Employee:
    """..."""

    def __init__(self, first_name, last_name, nianxin):
        """初始化"""
        self.first_name = first_name
        self.last_name = last_name
        self.nianxin = nianxin

    def give_raise(self, money=5000):
        """加工资"""
        self.nianxin += money


# a = Employee('tan', 'yao', 50000)
# a.give_raise(20000)
# print(a.nianxin)
