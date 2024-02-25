import requests
import os

class AuthUser:
    api_url = 'https://api.ullme.com/api/auth/login/'
    responce = None
    responce_json = None
    access_token = os.getenv("ACCESS_TOKEN")
    refresh_token = os.getenv("REFRESH_TOKEN")

    def auth_user(self, data):
        self.responce = requests.post(url=self.api_url, json = data)
        self.access_token = self.responce_json = self.responce.json()

        os.environ["REFRESH_TOKEN"] = self.responce_json['refresh']
        os.environ["ACCESS_TOKEN"] = self.responce_json['access']

        self.refresh_token = os.getenv("ACCESS_TOKEN")
        self.access_token = os.getenv("REFRESH_TOKEN")

        print(f'\n\nrefresh_token: {self.refresh_token}')
        print(f'\naccess_token: {self.access_token}')

        return self.responce.status_code

