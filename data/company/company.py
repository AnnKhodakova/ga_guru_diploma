import csv
import random
import os
from data import company


class Company:
    name: str
    phone: str
    activity: str
    capital_with_e: str
    capital_without_e: str
    csv_name: str = "company.csv"

    def __init__(self):
        with open(self.csv_path, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            row = random.choice(list(reader))
            for key, value in row.items():
                setattr(self, key, value)

    @property
    def csv_path(self):
        return os.path.abspath(os.path.join(os.path.dirname(company.__file__), self.csv_name))