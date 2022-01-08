import sys, socket
import time

from utils import Utils


class Client(Utils):

    def create_presence_message(self, account_name):
        message = {
            "action": "presence",
            "time": time.time(),
            "user": {
                "account_name": account_name
            }
        }
        return message

    def main(self):
        try:
            server_address = sys.argv[1]
            server_port = int(sys.argv[2])
            if not 65535 >= server_port >= 1024:
                raise ValueError
        except IndexError:
            server_address = '127.0.0.1'
            server_port = 7777
        except ValueError:
            print('Порт должен быть указан в пределах от 1024 до 65535')
            sys.exit(1)

        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        presence_message = self.create_presence_message('Guest')
        self.send_message(transport, presence_message)
        response = self.get_message(transport)
        handled_response = self.handle_message(response)
        print(f'Ответ от сервера: {response}')
        print(handled_response)


client = Client()


def main():
    client.main()


if __name__ == '__main__':
    main()
