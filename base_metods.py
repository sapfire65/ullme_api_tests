import requests
from faker import Faker

class Base:
    """Базовые методы для всего проекта"""

    def generate_fake_email():
        fake = Faker()

        email = fake.email()
        print(email)





Base.generate_fake_email()


