import pytest
import requests
from settings import *
from base_metods import APIMethods
from colorama import Fore, Style
before_text = Fore
after_text = Style.RESET_ALL


api_tests = APIMethods

def test_create_user():
    """Позитивный сценарий создание юзера

    e-mail: (str)
    password: (str)
    """
    json_res, responce = api_tests.add_new_user()

    print(f'\n\n{before_text.LIGHTYELLOW_EX}Responce:{after_text} \n{before_text.CYAN}status: {responce.status_code}, \nmasage: {responce.text}{after_text}\n')

    assert responce.status_code == 201, 'Статус кода не 201 !!!'
    assert json_res['email'] == CreateUser.email, 'Исходная почта и ответ, не совпадают !!!'
    assert json_res['id'] is not None, 'Нет присвоения ID'