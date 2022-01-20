import sys, socket
import time
import logging
import log.client_log_config
import log.decorator_log_config
from utils import Utils, logs

client_logger = logging.getLogger('client')


class Client(Utils):
    @logs
    def create_presence_message(self, account_name, msg_time=time.time()):
        client_logger.info('Создание сообщения для отправки на сервер...')
        message = {
            "action": "presence",
            "time": msg_time,
            "user": {
                "account_name": account_name
            }
        }

        return message

    @logs
    def write_message(self, sock, account_name):
        message = input('Введите сообщение для отправки или "Exit" для выхода из программы: ')
        if message == 'Exit':
            sock.close()
            client_logger.info('Соединение с сервером закрыто')
            sys.exit(0)
        client_logger.info('Создание сообщения для отправки на сервер...')
        message_from_client = {
            'action': 'message',
            'time': time.time(),
            'account_name': account_name,
            'message_text': message
        }
        return message_from_client

    @logs
    def get_message_from_server(self, message):
        if "action" in message \
             and message["action"] == "message" \
             and "time" in message \
             and "message_text" in message \
             and "sender" in message:
            print(f'Вы получили сообщение от {message["sender"]}: {message["message_text"]}')
        else:
            client_logger.error('Ошибка при получении сообщения с сервера')

    @logs
    def client_main(self):
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
        presence_message = self.create_presence_message('Guest')
        client_logger.info(f'Отправка сообщения {presence_message} серверу...')
        self.send_message(transport, presence_message)
        client_logger.info(f'Получение ответа от сервера...')
        response = self.get_message(transport)
        client_logger.info(f'Обработка сообщения от сервера...')
        handled_response = self.handle_message(response)
        print(handled_response)



