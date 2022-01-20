import json, sys, socket, select, logging
import time

import log.server_log_config
import log.decorator_log_config
from utils import Utils, logs

server_logger = logging.getLogger('server')


class Server(Utils):

    @logs
    def server_main(self):
        try:
            server_logger.info('Получение адреса и порта из параметров командной строки...')
            if '-p' in sys.argv:
                listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            else:
                listen_port = 7777
            if not 65535 >= listen_port >= 1024:
                raise ValueError
        except ValueError:
            server_logger.error('Неверный порт. Порт должен быть указан в пределах от 1024 до 65535')
            sys.exit(1)
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
        server_logger.info('Адрес и порт из параметров командной строки успешно получены!')
        server_logger.info('Создание сокета...')
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.bind((listen_address, listen_port))
        server_logger.info('Сокет успешно создан!')

        transport.listen(5)
        transport.settimeout(0.2)

        clients = []
        messages = []

        while True:
            try:
                client, client_address = transport.accept()
            except OSError:
                pass
            else:
                server_logger.info(f'Установка соединения с клиентом {client_address}...')
                clients.append(client)

            receives = []
            responses = []
            errors = []
            try:
                if clients:
                    receives, responses, errors = select.select(clients, clients, [], 0)
            except:
                pass

            if receives:
                server_logger.info(f'Получение сообщений от клиентов...')
                for client in receives:
                    try:
                        message = self.get_message(client)
                        messages.append([client, self.handle_message(message)])
                    except:
                        server_logger.info(f'Соединение с клиентом {client.getpeername()} закрыто')
                        clients.remove(client)

            if messages and responses:
                server_logger.info(f'Формирование сообщения...')
                send_message = {
                    'action': 'message',
                    'sender': messages[0][0],
                    'time': time.time(),
                    'message_text': messages[0][1]
                }
                del messages[0]
                for client in responses:
                    try:
                        self.send_message(client, send_message)
                    except:
                        server_logger.info(f'Соединение с клиентом {client.getpeername()} закрыто')
                        clients.remove(client)


server = Server()


def main():
    server.server_main()


if __name__ == '__main__':
    main()
