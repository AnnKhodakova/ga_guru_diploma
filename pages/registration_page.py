from selene import browser
from selene import be, by
from dotenv import load_dotenv
import random
import string
import os

load_dotenv()


def create_email():
    alias = "".join(random.choices(string.ascii_lowercase, k=6))
    return os.getenv("EMAIL_BODY") + alias + os.getenv("EMAIL_DOMAIN")


class RegistrationPage:
    def open(self):
        browser.open(os.getenv('DEV_SIGN_UP_LINK'))
        return self

    def registration(self):
        email = create_email()
        browser.all('.base-input-field__input')[0].should(be.visible).type(email)
        browser.all('.base-input-field__input')[1].should(be.visible).type(os.getenv("PASSWORD"))
        browser.element('.checkbox-inner').click()
        browser.element(by.text('Create Account')).click()
        return self
