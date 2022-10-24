from string import ascii_lowercase, digits
import random


class EmailValidator:
    CHARS_CORRECT = ascii_lowercase + digits + '._'

    def __new__(cls, *args, **kwargs):
        return None

    @staticmethod
    def __is_email_str(email):
        return type(email) == str

    @classmethod
    def check_email(cls, email: str):
        if cls.__is_email_str(email):
            email_lst = email.lower().split('@')
            if len(email_lst) != 2 or len(email_lst[0]) > 100 or len(email_lst[1]) > 50 or '..' in email_lst[0] or \
                    '..' in email_lst[1] or email_lst[1].count('.') == 0 or '_' in email_lst[1]:
                return False
            for ch in email_lst[0]:
                if ch not in cls.CHARS_CORRECT:
                    return False
            return True
        return False

    @classmethod
    def get_random_email(cls):
        length = random.randint(3, 100)
        rand_string = ''.join(random.choice(cls.CHARS_CORRECT) for i in range(length))
        return rand_string + '@gmail.com'


random_email = EmailValidator.get_random_email()
print(random_email)
print(EmailValidator.check_email(random_email))

print(EmailValidator.check_email("sc_lib@list.ru"))
print(EmailValidator.check_email("sc_lib@list_ru"))
print(EmailValidator.check_email("sc@lib@list_ru"))
print(EmailValidator.check_email("sc.lib@list_ru"))
print(EmailValidator.check_email("sclib@list.ru"))
print(EmailValidator.check_email("sc.lib@listru"))
print(EmailValidator.check_email("sc..lib@list.ru"))
