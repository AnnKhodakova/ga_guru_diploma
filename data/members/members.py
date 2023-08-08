import csv
import random
import os
from data import members


class Member:
    first_name: str
    last_name: str
    middle_name: str
    date_of_birth: str
    email: str
    phone_number: str
    city: str
    address: str
    postal_code: str
    document_number: str
    document_date: str
    picture_name: str
    csv_name: str = "member.csv"

    def __init__(self):
        with open(self.csv_path, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            row = random.choice(list(reader))
            for key, value in row.items():
                setattr(self, key, value)

    @staticmethod
    def _get_abspath(filename):
        return os.path.abspath(os.path.join(os.path.dirname(members.__file__), f"resourses/{filename}"))

    @property
    def csv_path(self):
        return self._get_abspath(self.csv_name)

    @property
    def picture_path(self):
        return self._get_abspath(self.picture_name)
