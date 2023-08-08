from selene import browser, be, have, by
from selenium.webdriver import Keys
import time
import random
import string


class Onboarding:

    def choose_estonia(self):
        browser.all(".radio-inner")[0].should(be.visible).click()
        browser.all(".radio-text")[0].should(have.text("Estonia"))
        browser.element(".bold-enabled").click()
        time.sleep(10)
        return self


    def choose_netherlands(self):
        browser.all(".radio-inner")[1].should(be.visible).click()
        browser.all(".radio-text")[1].should(have.text("Netherlands"))
        browser.element(".bold-enabled").click()
        time.sleep(10)
        return self

    def choose_transfer_est(self):
        browser.all(".radio-inner")[0].should(be.visible).click()
        browser.all(".radio-text")[0].should(have.text("I have or represent a company"))
        browser.element(by.text("Next")).click()
        return self

    def choose_incorporation(self):
        browser.all(".radio-inner")[1].should(be.visible).click()
        browser.all(".radio-text")[1].should(
            have.text("I am looking to open a company")
        )
        browser.all(".bold-enabled")[1].click()
        return self

    def request_incorporation_nl(self):
        browser.element(".link-request").click()
        browser.element(".questionnaire-success__button").click()
        browser.element(".close-icon").click()
        return self

    def choose_have_eres(self):
        browser.all(".radio-inner")[0].click()
        browser.all(".radio-text")[0].should(have.text("Yes"))
        browser.all(".bold-enabled")[1].click()
        return self

    def choose_not_have_eres(self):
        browser.all(".radio-inner")[1].click()
        browser.all(".radio-text")[1].should(have.text("No"))
        browser.all(".bold-enabled")[1].click()
        return self

    def skip_for_now(self):
        browser.element(by.text("Skip for now")).click()
        return self

    def start_incorporation_no_e(self):
        browser.element(".card__price").should(be.visible).should(have.text("€1090"))
        browser.element(".buttons__top").click()
        return self

    def start_incorporation_e(self):
        browser.element(".card__price").should(be.visible).should(have.text("€350"))
        browser.element(".buttons__top").click()
        return self

    def company_transfer_nl(self):
        browser.element(".sub-header").should(have.text("Dutch register"))
        self.find_company_name_onboarding()

    def confirm_transfer(self):
        browser.element(".questionnaire-success-nl__desc").should(
            have.text("was connected to Enty!")
        )
        browser.element(".learn-why-btn").click()
        return self

    def company_transfer_est(self):
        browser.element(".sub-header").should(have.text("Estonian register"))
        self.find_company_name_onboarding()

    def find_company_name_onboarding(self):
        while True:
            part_of_name = "".join(random.choices(string.ascii_lowercase, k=3))
            input_field = browser.element(".input").type(part_of_name)
            if browser.element(".suggestion").wait_until(be.visible):
                browser.all(".suggestion-item")[0].click()
                if browser.element(".e-success").wait_until(be.visible):
                    browser.element(".action.action__pink").click()
                    break
            input_field.send_keys(Keys.CONTROL + "a")
        return self

    def find_company_name_modalka(self):
        while True:
            part_of_name = "".join(random.choices(string.ascii_lowercase, k=3))
            input_field = browser.element(".input").type(part_of_name)
            if browser.element(".suggestion").wait_until(be.visible):
                browser.all(".suggestion-item")[0].click()
                if browser.element(".e-success").wait_until(be.visible):
                    browser.element(".btn-component").click()
                    break
            input_field.send_keys(Keys.CONTROL + "a")
        return self
