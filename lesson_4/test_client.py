import unittest
from client import client


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
    OK = '200 : OK'
    error = 'Bad Request'

    def test_create_presence_message(self):
        self.assertEqual(client.create_presence_message('Guest', 1.2), self.presence_message)

    def test_get_correct_answer(self):
        self.assertEqual(client.handle_message(self.correct_answer), self.OK)

    def test_get_bad_request(self):
        self.assertEqual(client.handle_message(self.bad_request), self.error)


if __name__ == '__main__':
    unittest.main()
