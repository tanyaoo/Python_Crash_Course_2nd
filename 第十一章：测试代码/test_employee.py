import unittest
from employee import Employee


class TestEmployeeCase(unittest.TestCase):
    """测试"""

    def setUp(self):
        """创建对象属性，供方法使用"""
        self.employee_a = Employee('tan', 'yao', 10000)

    def test_give_default_raise(self):
        """测试default"""
        self.employee_a.give_raise()
        self.assertEqual(self.employee_a.nianxin, 15000)

    def test_give_custom_raise(self):
        """测试custom"""
        self.employee_a.give_raise(10000)
        self.assertEqual(self.employee_a.nianxin, 20000)
