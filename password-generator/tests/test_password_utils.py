import unittest
from utils.password_utils import calculate_password_strength

class TestPasswordUtils(unittest.TestCase):
    def test_calculate_password_strength(self):
        self.assertEqual(calculate_password_strength("abc"), "Weak")
        self.assertEqual(calculate_password_strength("abc123"), "Weak")
        self.assertEqual(calculate_password_strength("abc123!@#"), "Medium")
        self.assertEqual(calculate_password_strength("ABCabc123!@#"), "Strong")

if __name__ == "__main__":
    unittest.main()