import requests
import json
from data.data_base import Data

class Delete:
    url = "https://api.ullme.com/api/users/me/"

    def delete_user(self, password, access_token):
        user_email = Data()
        payload = json.dumps({
            "current_password": password
        })
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        response = requests.request("DELETE", self.url, headers=headers, data=payload)
        print()
        print(f'Юзер: {user_email.email} > удален, статус код: {response.status_code}')
        return response.status_code


