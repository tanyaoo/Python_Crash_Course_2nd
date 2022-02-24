import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """测试name_function.py"""
    def test_first_last_name(self):
        """能够正确地处理像tan yao这样的姓名吗？"""
        formatted_name = get_formatted_name('ma', 'teng', 'hua')
        self.assertEqual(formatted_name, 'Ma Hua Teng')


if __name__ == '_main_':
    unittest.main()

