import json, sys, socket

from utils import Utils


class Server(Utils):

    def main(self):
        try:
            if '-p' in sys.argv:
                listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            else:
                listen_port = 7777
            if not 65535 >= listen_port >= 1024:
                raise ValueError
        except ValueError:
            print('Порт должен быть указан в пределах от 1024 до 65535')
            sys.exit(1)
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.bind((listen_address, listen_port))

        transport.listen(5)
        while True:
            client, client_address = transport.accept()
            try:
                message = self.get_message(client)
                response = self.handle_message(message)
                self.send_message(client, response)
                client.close()
            except (ValueError, json.JSONDecodeError):
                print('Принято некорректное сообщение от клиента')
                client.close()


server = Server()


def main():
    server.main()


if __name__ == '__main__':
    main()
