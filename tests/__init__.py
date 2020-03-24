import random
import string
import json

def generate_user_id():
    """
    for a user, generate a unique id of 238 characters
    :return: user_id: str
    """
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(letters) for i in range(128))


class User(object):
    def __init__(self, username, password, email, user_id=None):
        self.username = username
        self.password = password
        self.email = email
        if user_id:
            self.user_id = user_id
        else:
            self.user_id = generate_user_id()

    def __str__(self):
        return self.__dict__.__str__()

    def get_json(self):
        return self.__dict__.__str__()  # talking about tricks :))





# from os import listdir
# from base64 import b64encode, b64decode
# fns = listdir('./imgs')
# for fn in fns:
#     b64 = b64encode(open('./imgs/' + fn, 'rb').read())
#     print(b64)
#     with open('./txts/' + fn[:-3] + 'txt', 'w') as file:
#         file.write(str(b64))
import requests



admin_1 = User('admin1', 'password1', 'admin1@xscanner.ro', '1' * 128)
admin_2 = User('admin2', 'password2', 'admin2@xscanner.ro', '2' * 128)
admin_3 = User('admin3', 'password3', 'admin3@xscanner.ro', '3' * 128)
