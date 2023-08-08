from selene.support.shared import browser
from selene import be, command, have
from data.company import company

browser.config.hold_browser_open = True
browser.config.timeout = 40.0
browser.config.wait_for_no_overlap_found_by_js = True


class CompanyInformationPage:
    company = company.Company()

    company_name = browser.element('[placeholder="Company Name"]')
    company_phone = browser.element('[placeholder="Company Phone"]')
    next_button = browser.element('.action-button')

    def type_company_name(self):
        self.company_name.should(be.visible).type(self.company.name)
        self.next_button.perform(command.js.scroll_into_view)
        return self

    def choose_main_field_of_activity(self):
        browser.element('.company-name-success').wait_until(be.visible)
        browser.element('[placeholder="Main field of activity"]').with_(click_by_js=True).click()
        browser.all('.base-select__dropdown--content_item')[0].with_(click_by_js=True).click()
        return self

    def choose_activity_code(self):
        browser.element('[placeholder="Activity code"]').with_(click_by_js=True).click()
        browser.all('.base-select__dropdown--content_item')[0].with_(click_by_js=True).click()
        return self

    def choose_phone_code(self):
        browser.element('[placeholder="Code"]').with_(click_by_js=True).click()
        browser.all('.base-select__dropdown--content_item')[0].with_(click_by_js=True).click()
        return self

    def type_company_phone(self):
        browser.element('[placeholder="Company Phone"]').type(self.company.phone)
        return self

    def type_information_about_company_activity(self):
        browser.all('.input')[3].should(be.visible).type(self.company.activity).wait_until(be.not_.blank)
        return self

    def should_have_information(self, capital):
        self.company_name.perform(command.js.scroll_into_view)
        self.company_name.should(have.value(self.company.name))
        self.next_button.perform(command.js.scroll_into_view)
        self.company_phone.should(have.value(self.company.phone))
        browser.all('.input')[3].should(have.value(self.company.activity))
        browser.element('[placeholder="Share Capital, EUR"]').should(have.value(capital))
        return self

    def go_to_next_step(self):
        browser.element('.action-button').perform(command.js.scroll_into_view)
        browser.element('.action-button').should(be.visible).click()
        return self
