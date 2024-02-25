import re
import time
from time import sleep

import requests
from faker import Faker
from imap_tools import MailBox, AND
import re

class Data:

    activate_linc = None
    imap_url = 'imap.gmail.com'

    email = 'alexandr.cherenkov.worck@gmail.com'
    email_password = 'uhkj xhww rcxz sodk'
    password = 'Asd#555'


    """Базовые методы для всего проекта"""

    @staticmethod
    def reqular_findall(text, before_text, after_text):
        """Регулярное выражение, возвращает список элементов между двумя отрезками строк

            :param text: (str), исходный текст
            :param before_text: (str), фрагмент строки "до" искомого элемента
            :param after_text: (str), фрагмент строки "после" искомого элемента
            """

        return re.findall(fr'{before_text}(.*?){after_text}', text)


    def check_mail_and_activation(self, timeout = 10, check_frequency=1):

        def check_mail(self):
            """Проверка получения письма по части названия и получение ссылки активации"""
            email_name = self.email
            email_password = self.email_password

            with MailBox(self.imap_url).login(email_name, email_password) as mailbox:
                for msg in mailbox.fetch(AND(subject='api.ullme.com', seen=False, flagged=False), limit=1,
                                         reverse=True):
                    text = msg.text
                    text_without_spaces = re.sub(r"\s+", "", text)
                    self.activate_linc = self.reqular_findall(
                        text_without_spaces,
                        before_text='activateaccount:',
                        after_text='Thanks')[0]
                    return self.activate_linc

        def wite_email_and_activation(self):
            """Ожидание письма по таймауту, и переход по ссылке активации"""
            start_time = time.time()

            while (time.time() - start_time) < timeout:
                if self.activate_linc is None:
                    print('| status:',self.activate_linc, time.strftime('%H:%M:%S'))
                    check_mail(self)
                    sleep(check_frequency)

                else:
                    if self.activate_linc is None:
                        print('Ожидание письма завершено, ссылки на активацию нет',
                              'status:', self.activate_linc)
                        break

                    else:
                        print('| status: OK', time.strftime('%H:%M:%S'))
                        print()
                        print('GET from:', self.activate_linc)
                        responce = requests.get(self.activate_linc)
                        print(f'Статус код активации E-mail по ссылке: {responce.status_code}')
                        return responce.status_code

        wite_email_and_activation(self)





#     def generate_fake_email():
#         fake = Faker()
#
#         email = fake.email()
#         print(email)
#
# Base.generate_fake_email()


