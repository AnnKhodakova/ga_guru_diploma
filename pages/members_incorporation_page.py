import time
from selene import browser, be, have, command, by
from data.members import members


class MembersPage:
    member = members.Member()

    def add_member_no_e(self):
        browser.element('.shareholder').click()
        browser.element('[placeholder="First Name"]').should(be.visible).type(self.member.first_name)
        browser.element('[placeholder="Last Name"]').should(be.visible).type(self.member.last_name)
        browser.element('[placeholder="Middle Name (Optional)"]').should(be.visible).type(self.member.middle_name)
        browser.all('.base-input-field__input')[0].should(be.visible).type(self.member.date_of_birth)
        browser.element('[placeholder="Code"]').should(be.visible).click()
        browser.all('.base-select__dropdown--content_item')[0].should(be.visible).click()
        browser.element('[placeholder="Phone number"]').should(be.visible).type(self.member.phone_number)
        browser.element('[placeholder="Postal Code"]').perform(command.js.scroll_into_view)
        browser.element('[placeholder="Select Country"]').should(be.visible).click()
        browser.all('.base-select__dropdown--content_item')[0].should(be.visible).click()
        browser.element('[placeholder="City"]').should(be.visible).type(self.member.city)
        browser.element('[placeholder="Address"]').should(be.visible).type(self.member.address)
        browser.element('[placeholder="Postal Code"]').type(self.member.postal_code)
        browser.element('.input-file').perform(command.js.scroll_into_view)
        browser.element('[placeholder="Document type"]').click()
        browser.all('.base-select__dropdown--content_item')[0].click()
        browser.all('.input')[9].type(self.member.document_number)
        browser.all('.base-input-field__input')[1].should(be.visible).type(self.member.document_date)
        browser.element('.tokenize-input').send_keys(self.member.picture_path).wait_until(be.visible)
        browser.element(by.text('Save')).click()
        return self

    def add_member_with_e(self):
        browser.element('.shareholder').click()
        browser.element('[placeholder="First Name"]').type(self.member.first_name)
        browser.element('[placeholder="Last Name"]').type(self.member.last_name)
        browser.element('.base-input-field__input').type(self.member.date_of_birth)
        browser.element('[placeholder="Code"]').click()
        browser.all('.base-select__dropdown--content_item')[0].click()
        browser.element('[placeholder="Phone number"]').type(self.member.phone_number)
        browser.all('.input')[8].perform(command.js.scroll_into_view)
        browser.element('[placeholder="Select Country"]').click()
        browser.all('.base-select__dropdown--content_item')[0].click()
        browser.element('[placeholder="City"]').type(self.member.city)
        browser.element('[placeholder="Address"]').type(self.member.address)
        browser.element('[placeholder="Postal Code"]').type(self.member.postal_code)
        browser.element('[placeholder="Digital ID type"]').click()
        browser.all('.base-select__dropdown--content_item')[0].click()
        browser.all('.input')[8].type(self.member.document_number).wait_until(be.not_.blank)
        browser.element('.bold-enabled').click()
        return self

    def first_member_should_be_added(self):
        browser.element('.shareholder__text').element('.text__title').should(have.text(self.member.first_name))
        return self

    def go_to_next_page(self):
        browser.element('.checkbox-inner').click()
        time.sleep(5)
        browser.element(by.text('Next')).perform(command.js.scroll_into_view)
        browser.element(by.text('Next')).click()
        browser.all('.incorporation-step-info')[2].perform(command.js.scroll_into_view)
        browser.all('.incorporation-step-info__logo')[2].click()
        return self

    def reset_application(self):
        browser.element('.reset-application').click()
        return self
