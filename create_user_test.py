import pytest
import requests
from colorama import Fore, Style

before_text = Fore
after_text = Style.RESET_ALL



class TestCreateUser:
    """Тесты создания юзеров"""
    url = 'https://api.ullme.com/api/users/'
    email = 'sapfiretrey@gmail.com'
    password = 'Asd#555'

    def test_create_user(self):
        """Позитивный сценарий создание юзера

        e-mail: (str)
        password: (str)
        """
        api_url = self.url

        data = {
            'email': f'{self.email}',
            'password': f'{self.password}'
        }

        responce = requests.post(api_url, json = data)
        json_format = responce.json()

        print(f'\n\n{before_text.LIGHTYELLOW_EX}Responce:{after_text} \n{before_text.CYAN}status: {responce.status_code}, \nmasage: {responce.text}{after_text}\n')

        assert responce.status_code == 201, 'Статус кода не 201 !!!'
        assert json_format['email'] == self.email, 'Исходная почта и ответ, не совпадают !!!'
        assert json_format['id'] is not None, 'Нет присвоения ID'




