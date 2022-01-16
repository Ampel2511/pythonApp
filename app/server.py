import json, sys, socket
import logging
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
        while True:
            client, client_address = transport.accept()
            server_logger.info(f'Установка соединения с клиентом {client}...')
            try:
                server_logger.info(f'Получение сообщения от клиента {client}...')
                message = self.get_message(client)
                response = self.handle_message(message)
                server_logger.info(f'Обработка сообщения от клиента {client}...')
                self.send_message(client, response)
                server_logger.info('Отправка ответа...')
                client.close()
                server_logger.info(f'Соединение с клиентом {client} закрыто')
            except (ValueError, json.JSONDecodeError):
                server_logger.error('Принято некорректное сообщение от клиента')
                client.close()


server = Server()


def main():
    server.server_main()


if __name__ == '__main__':
    main()
