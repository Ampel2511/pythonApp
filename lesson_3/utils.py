import json


class Utils:
    def send_message(self, opened_socket, message):
        json_message = json.dumps(message)
        response = json_message.encode("utf-8")
        opened_socket.send(response)

    def get_message(self, opened_socket):
        response = opened_socket.recv(1024)
        if isinstance(response, bytes):
            json_response = response.decode("utf-8")
            response_dict = json.loads(json_response)
            if isinstance(response_dict, dict):
                return response_dict
            raise ValueError
        raise ValueError

    def handle_message(self, message):
        if "response" in message:
            if message["response"] == 200:
                return '200 : OK'
            return f'400 : {message["error"]}'

        elif "action" in message \
                and message["action"] == "presence" \
                and "time" in message \
                and "user" in message \
                and message["user"]["account_name"] == 'Guest':
            return {"response": 200}
        return {
            "response": 400,
            "error": 'Bad Request'
        }
