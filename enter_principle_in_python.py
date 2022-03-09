class LifePrinciple:
    """生活原则"""

    def __init__(self, name):
        """初始化类，并指明是谁的生活原则"""
        self.name = name

    def who_principle(self):
        """指出是谁的生活原则"""
        print(f'This is {self.name}`s life principle')

    def the_basic_principle(self):
        """最基本的原则"""
        unit_1 = '1、你想要什么？'
        unit_2 = '2、事实是什么？'
        unit_3 = '3、面对事实，你如何实现自己的愿望？'
        units = [unit_1, unit_2, unit_3]

        for unit in units:
            print(unit)


my_principle = LifePrinciple("tanyao")
my_principle.the_basic_principle()
