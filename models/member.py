import random

class User:
    def __init__(self, name, id=random.randint(1, 500), books=[]):
        self.name = name
        self.id = id
        self.books = books
    def to_dict(self):
        return self.__dict__
    def find_indexU(self, users, user_name):
        for i, user in enumerate(users):
            if user['name'] == user_name:
                return i