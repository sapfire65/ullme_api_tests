import re
import time
from time import sleep

import requests
from faker import Faker
from imap_tools import MailBox, AND, A


class Data:

    activate_linc = None
    imap_url = 'imap.gmail.com'

    email = 'alexandr.cherenkov.worck@gmail.com'
    email_password = 'uhkj xhww rcxz sodk'
    password = 'Asd#555'
    key_in_header_email = 'api.ullme.com'
    wite_timeout = 90


    """Базовые методы для всего проекта"""

    @staticmethod
    def reqular_findall(text, before_text, after_text):
        """Регулярное выражение, возвращает список элементов между двумя отрезками строк

            :param text: (str), исходный текст
            :param before_text: (str), фрагмент строки "до" искомого элемента
            :param after_text: (str), фрагмент строки "после" искомого элемента
            """

        return re.findall(fr'{before_text}(.*?){after_text}', text)


    def check_mail_and_activation(self):

        def deleting_mail_with_header_key(self, mesage = 'Письмо удалено'):
            email_name = self.email
            email_password = self.email_password

            with MailBox(self.imap_url).login(email_name, email_password) as mailbox:
                responce = mailbox.delete(
                    [msg.uid for msg in mailbox.fetch() if self.key_in_header_email in msg.html])
                if responce is not None:
                    status =  str(responce)
                    status = status.replace(')', '').split()[4]
                    print(f'\n{mesage}, статус:', status)
                    return status

                else:
                    print('Писем по заданным критериям нет\n')



        def wite_email_and_activation(self):
            """Проверка получения письма по части названия и получение ссылки активации"""
            email_name = self.email
            email_password = self.email_password

            with MailBox(self.imap_url).login(email_name, email_password) as mailbox:
                print('Ожидание письма и ссылки активации')

                responses = mailbox.idle.wait(timeout=self.wite_timeout)

                if responses:
                    for msg in mailbox.fetch(AND(subject=self.key_in_header_email, seen=False, flagged=False), limit=1,
                                             reverse=True):
                        text = msg.text
                        text_without_spaces = re.sub(r"\s+", "", text)
                        self.activate_linc = self.reqular_findall(
                            text_without_spaces,
                            before_text='activateaccount:',
                            after_text='Thanks')[0]

                        print('| status: OK', time.strftime('%H:%M:%S'))
                        print()
                        print('GET from:', self.activate_linc)
                        responce = requests.get(self.activate_linc)
                        assert responce.status_code == 200, 'Ошибка перехода по ссылке ативации'
                        print(f'Статус код активации E-mail по ссылке: {responce.status_code}')
                        return responce.status_code

                else:
                    assert responses is None, 'Ожидание письма завершино, ссылки активации нет.'



        deleting_mail_with_header_key(self, 'Старые письма удалены')# Удаление старых писем, если будут
        wite_email_and_activation(self)
        deleting_mail_with_header_key(self, 'Письмо с сылкой активации удалено') # Удаление нового письма






#     def generate_fake_email():
#         fake = Faker()
#
#         email = fake.email()
#         print(email)
#
# Base.generate_fake_email()


