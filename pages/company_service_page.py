from selene import browser, command, have


class CompanyServicePage:
    def choose_incorporation_with_e(self):
        browser.all('.card-button')[1].perform(command.js.scroll_into_view)
        browser.all('.card-button')[1].click()
        browser.element('.btn-component').click()
        return self

    def choose_incorporation_without_e(self):
        browser.all('.card-button')[2].perform(command.js.scroll_into_view)
        browser.all('.card-button')[2].click()
        return self

    def go_to_company(self):
        browser.element('.company-info-area').click()
        return self

    def go_to_company_from_navigation(self):
        browser.all('.navigation__item')[1].hover()
        browser.all('.route-name')[0].click()

    def choose_transfer(self):
        browser.all('.card-button')[0].click()
        return self

    def confirm_transfer_from_service(self):
        browser.element('.questionnaire-success-nl__desc').should(have.text('was connected to Enty!'))
        browser.element('.learn-why-btn').click()
        return self
