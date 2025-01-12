import unittest
from core.nlp_processor import process_input

class TestNLPProcessor(unittest.TestCase):
    def test_process_input(self):
        user_input = "What is the capital of France?"
        response = process_input(user_input)
        self.assertIn("Paris", response)

if __name__ == "__main__":
    unittest.main()