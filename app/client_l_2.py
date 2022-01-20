import sys, socket
import time
import logging
import log.client_log_config
import log.decorator_log_config
from utils import Utils, logs
from client import Client

client_logger = logging.getLogger('client')


class ClientListen(Client):

    @logs
    def client_listen_main(self):
        try:
            client_logger.info('Получение адреса и порта из параметров командной строки...')
            server_address = sys.argv[1]
            server_port = int(sys.argv[2])
            if not 65535 >= server_port >= 1024:
                raise ValueError
        except IndexError:
            client_logger.info('Установки параметров соединения по умолчанию...')
            server_address = '127.0.0.1'
            server_port = 7777
        except ValueError:
            client_logger.error('Неверный порт. Порт должен быть указан в пределах от 1024 до 65535')
            sys.exit(1)
        client_logger.info('Создание сокета и установка соединения...')
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.connect((server_address, server_port))
        client_logger.info(f'Отправка сообщения "presence" серверу...')
        self.send_message(transport, self.create_presence_message('Guest'))
        client_logger.info(f'Получение ответа от сервера...')
        response = self.get_message(transport)
        client_logger.info(f'Обработка сообщения от сервера...')
        handled_response = self.handle_message(response)
        print(handled_response)
        self.get_message_from_server(self.get_message(transport))


client_listen = ClientListen()


def main():
    client_listen.client_listen_main()


if __name__ == '__main__':
    main()