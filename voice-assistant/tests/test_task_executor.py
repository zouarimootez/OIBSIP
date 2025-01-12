import unittest
from core.task_executor import execute_task

class TestTaskExecutor(unittest.TestCase):
    def test_weather_task(self):
        intent = "What's the weather in New York?"
        response = execute_task(intent)
        self.assertIn("temperature", response)

    def test_email_task(self):
        intent = "Send an email."
        response = execute_task(intent)
        self.assertEqual(response, "Email sent!")

if __name__ == "__main__":
    unittest.main()