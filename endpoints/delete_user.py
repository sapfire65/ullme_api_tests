import requests
import json

class Delete:
    url = "https://api.ullme.com/api/users/me/"

    def delete_user(self, password, access_token):
        payload = json.dumps({
            "current_password": password
        })
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }

        response = requests.request("DELETE", self.url, headers=headers, data=payload)
        print()
        print(f'Статус код удаления: {response.status_code}')
        return response.status_code


