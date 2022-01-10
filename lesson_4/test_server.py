import unittest
from server import server


class TestClass(unittest.TestCase):
    presence_message = {
        "action": "presence",
        "time": 1.2,
        "user": {
            "account_name": 'Guest'
        }
    }
    correct_answer = {"response": 200}
    bad_request = {
        "response": 400,
        "error": 'Bad Request'
    }

    def test_get_correct_message(self):
        self.assertEqual(server.handle_message(self.presence_message), self.correct_answer)

    def test_get_wrong_message(self):
        self.assertEqual(server.handle_message({}), self.bad_request)


if __name__ == '__main__':
    unittest.main()
