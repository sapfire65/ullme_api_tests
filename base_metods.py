from typing import Dict
import requests
from faker import Faker
from settings import CreateUser
# class Base:
#     """Базовые методы для всего проекта"""
#
#     def generate_fake_email():
#         fake = Faker()
#
#         email = fake.email()
#         print(email)
#
# Base.generate_fake_email()

class APIMethods():

    def add_new_user():
       """Cценарий создание юзера

        e-mail: (str)
        password: (str)
        """
       data = {
           'email': f'{CreateUser.email}',
        'password': f'{CreateUser.password}'
       }

       responce = requests.post(CreateUser.api_url, json=data)
       json_res = responce.json()

       return json_res, responce

