import unittest
from city_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试"""

    def test_city_country(self):
        """测试格式是否正确"""
        formatted_name = get_formatted_name('beijing', 'china')
        self.assertEqual(formatted_name, 'Beijing China')

    def test_city_country_population(self):
        """测试有人口的格式"""
        formatted_name = get_formatted_name('santiago', 'chile', population=50000)
        # print(formatted_name)
        self.assertEqual(formatted_name, 'Santiago Chile - Population 50000')


if __name__ == '_main_':
    unittest.main()
