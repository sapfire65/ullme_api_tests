import requests
from colorama import Fore, Style

before_text = Fore
after_text = Style.RESET_ALL


class CreateUser:
    responce = None
    responce_json = None
    api_url = 'https://api.ullme.com/api/users/'

    def create_user(self, data):
        """
        e-mail: (str)
        password: (str)
        """

        self.responce = requests.post(self.api_url, json = data)
        self.responce_json = self.responce.json()

        print(f'\n\n{before_text.LIGHTYELLOW_EX}'
              f'Responce:{after_text} \n{before_text.CYAN}'
              f'status: {self.responce.status_code}, '
              f'\nmasage: {self.responce.text}{after_text}\n')

    def check_status_code(self, status_code):
        assert self.responce.status_code == status_code, f'Статус кода не {status_code} !!!'

    def check_email(self, email):
        assert self.responce_json['email'] == email, 'Исходная почта и ответ, не совпадают !!!'


    def check_id_is_not_none(self):
        assert self.responce_json['id'] is not None, 'Нет присвоения ID'





