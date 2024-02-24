import pytest
import os
from endpoints.create_user import CreateUser
from endpoints.auth_user import AuthUser
from data.data_base import Data
from endpoints.delete_user import Delete
from time import sleep

class TestCreateUser:

    email = Data.email
    password = Data.password

    refresh_token = None
    access_token =  None


    def test_create_user(self):
        data = {
            'email': f'{self.email}',
            'password': f'{self.password}'
        }

        create_user = CreateUser()
        create_user.create_user(data=data)
        create_user.check_status_code(201)
        create_user.check_email(self.email)
        create_user.check_id_is_not_none()

        sleep(3)

        activation = Data()
        activation.activation_mail()

        auth_user = AuthUser()
        auth_user.auth_user(data=data)
        self.access_token = os.getenv("ACCESS_TOKEN")

        delete = Delete()

        delete.delete_user(
            password=self.password,
            access_token=self.access_token
        )



