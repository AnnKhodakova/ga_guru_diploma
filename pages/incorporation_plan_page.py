from selene import browser
from selene import be, have, by, command
import time


class IncorporationPlanPage:
    def should_have_texts_when_no_e(self):
        browser.all('.subtitle-text')[0].should(have.text('Incorporation in Estonia without e-Residency'))
        browser.all('.subtitle-text')[1].should(have.text('Company Formation Government Fee'))
        return self

    def should_have_texts_when_e(self):
        browser.all('.subtitle-text')[0].should(have.text('Incorporation in Estonia with e-Residency'))
        browser.all('.subtitle-text')[1].should(have.text('Company Formation Government Fee'))
        return self

    def choose_standard_plan(self):
        browser.element('.choose-plan-button').click()
        browser.all('.main-pricing-table-container-column-buy-button')[2].click()
        return self

    def pay_incorporation_no_e_in_chargebee(self):
        browser.element('.pay-button').perform(command.js.scroll_into_view).wait_until(
            lambda driver: driver.find_element_by_css_selector('.pay-button').is_displayed())
        browser.element('.pay-button').should(be.visible).click().wait_until(be.visible)
        browser.driver.switch_to.frame('cb-frame')
        browser.all('.cb-item__middle')[1].should(be.visible).should(have.text('€290.00'))
        browser.all('.cb-item__middle')[2].should(have.text('€800.00'))
        browser.element('.cb-button__text').click()
        browser.all('.cb-field__control')[0].type('first')
        browser.all('.cb-field__control')[1].type('last')
        browser.element('.cb-button__text').should(be.visible).click()
        browser.all('.cb-field__control')[0].type('first')
        browser.all('.cb-field__control')[1].type('last')
        browser.all('.cb-field__control')[2].type('address1')
        browser.all('.cb-field__control')[3].type('address2')
        browser.all('.cb-field__control')[4].type('city')
        browser.all('.cb-field__control')[5].type('zip')
        browser.all('.cb-field__control')[6].type('state')
        browser.element('[id="country"]').click().send_keys('Aland Islands')
        browser.element('.cb-button__text').click()
        browser.all('.cb-options__right')[0].click()
        browser.all('[class^=cb-field__control]')[0].click()
        browser.element('.cb-pmcard__title').click()
        browser.element('.cb-button__text').click()
        browser.all('.cb-bar__aside')[0].should(have.text('€1,594.00'))
        browser.all('.cb-bar__aside')[1].should(have.text('€504.00'))
        browser.element('.cb-subscribe__check').click()
        browser.element('.cb-button__text').click()
        browser.element(by.text('CLOSE')).should(be.visible).click().wait_until(be.visible)
        browser.driver.switch_to.default_content()
        time.sleep(10)
        return self

    def confirm_payment_no_e(self):
        browser.element('.company-incorporation-success__btn').perform(command.js.scroll_into_view)
        browser.element('.company-incorporation-success-subtitle').should(have.text('€1594 Paid'))
        browser.element('.company-incorporation-success__btn').click()
        return self

    def pay_incorporation_with_digital_id_in_chargebee(self):
        browser.element('.pay-button').perform(command.js.scroll_into_view).wait_until(
            lambda driver: driver.find_element_by_css_selector('.pay-button').is_displayed())
        browser.element('.pay-button').should(be.visible).click().wait_until(be.visible)
        browser.driver.switch_to.frame('cb-frame')
        browser.all('.cb-item__middle')[1].should(be.visible).should(have.text('€290.00'))
        browser.all('.cb-item__middle')[2].should(have.text('€60.00'))
        browser.element('.cb-button__text').click()
        browser.all('.cb-field__control')[0].type('first')
        browser.all('.cb-field__control')[1].type('last')
        browser.element('.cb-button__text').should(be.visible).click()
        browser.all('.cb-field__control')[0].type('first')
        browser.all('.cb-field__control')[1].type('last')
        browser.all('.cb-field__control')[2].type('address1')
        browser.all('.cb-field__control')[3].type('address2')
        browser.all('.cb-field__control')[4].type('city')
        browser.all('.cb-field__control')[5].type('zip')
        browser.all('.cb-field__control')[6].type('state')
        browser.element('[id="country"]').click().send_keys('Aland Islands')
        browser.element('.cb-button__text').click()
        browser.all('.cb-options__right')[0].click()
        browser.all('[class^=cb-field__control]')[0].click()
        browser.element('.cb-pmcard__title').click()
        browser.element('.cb-button__text').click()
        browser.all('.cb-bar__aside')[0].should(have.text('€854.00'))
        browser.all('.cb-bar__aside')[1].should(have.text('€504.00'))
        browser.element('.cb-subscribe__check').click()
        browser.element('.cb-button__text').click()
        browser.element(by.text('CLOSE')).should(be.visible).click().wait_until(be.visible)
        browser.driver.switch_to.default_content()
        time.sleep(10)
        return self

    def confirm_payment_with_digital_id(self):
        browser.element('.company-incorporation-success__btn').perform(command.js.scroll_into_view)
        browser.element('.company-incorporation-success-subtitle').should(have.text('€854 Paid'))
        browser.element('.company-incorporation-success__btn').click()
        return self

    def should_have_texts_with_extra_member_e(self):
        browser.all('.subtitle-text')[0].should(have.text('Incorporation in Estonia with e-Residency'))
        browser.all('.subtitle-text')[1].should(have.text('Company Formation Government Fee'))
        browser.element('.shareholders-amount').should(have.text('€100 x 1'))
        return self

    def should_have_texts_with_extra_member_no_e(self):
        browser.all('.subtitle-text')[0].should(have.text('Incorporation in Estonia without e-Residency'))
        browser.all('.subtitle-text')[1].should(have.text('Company Formation Government Fee'))
        browser.element('.shareholders-amount').should(have.text('€100 x 1'))
        return self

    def pay_incorporation_with_e_in_chargebee(self):
        browser.element('.pay-button').perform(command.js.scroll_into_view).wait_until(
            lambda driver: driver.find_element_by_css_selector('.pay-button').is_displayed())
        browser.element('.pay-button').should(be.visible).click().wait_until(be.visible)
        browser.driver.switch_to.frame('cb-frame')
        browser.all('.cb-item__middle')[1].should(be.visible).should(have.text('€100.00'))
        browser.all('.cb-item__middle')[2].should(be.visible).should(have.text('€290.00'))
        browser.all('.cb-item__middle')[3].should(have.text('€60.00'))
        browser.element('.cb-button__text').click()
        browser.all('.cb-field__control')[0].type('first')
        browser.all('.cb-field__control')[1].type('last')
        browser.element('.cb-button__text').should(be.visible).click()
        browser.all('.cb-field__control')[0].type('first')
        browser.all('.cb-field__control')[1].type('last')
        browser.all('.cb-field__control')[2].type('address1')
        browser.all('.cb-field__control')[3].type('address2')
        browser.all('.cb-field__control')[4].type('city')
        browser.all('.cb-field__control')[5].type('zip')
        browser.all('.cb-field__control')[6].type('state')
        browser.element('[id="country"]').click().send_keys('Aland Islands')
        browser.element('.cb-button__text').click()
        browser.all('.cb-options__right')[0].click()
        browser.all('[class^=cb-field__control]')[0].click()
        browser.element('.cb-pmcard__title').click()
        browser.element('.cb-button__text').click()
        browser.all('.cb-bar__aside')[0].should(have.text('€954.00'))
        browser.all('.cb-bar__aside')[1].should(have.text('€504.00'))
        browser.element('.cb-subscribe__check').click()
        browser.element('.cb-button__text').click()
        browser.element(by.text('CLOSE')).should(be.visible).click().wait_until(be.visible)
        browser.driver.switch_to.default_content()
        time.sleep(10)
        return self

    def confirm_payment_with_e(self):
        browser.element('.company-incorporation-success__btn').perform(command.js.scroll_into_view)
        browser.element('.company-incorporation-success-subtitle').should(have.text('€954 Paid'))
        browser.element('.company-incorporation-success__btn').click()
        return self

    def pay_incorporation_with_extra_member_no_e_in_chargebee(self):
        browser.element('.pay-button').perform(command.js.scroll_into_view).wait_until(
            lambda driver: driver.find_element_by_css_selector('.pay-button').is_displayed())
        browser.element('.pay-button').should(be.visible).click().wait_until(be.visible)
        browser.driver.switch_to.frame('cb-frame')
        browser.all('.cb-item__middle')[1].should(be.visible).should(have.text('€100.00'))
        browser.all('.cb-item__middle')[2].should(be.visible).should(have.text('€290.00'))
        browser.all('.cb-item__middle')[3].should(have.text('€800.00'))
        browser.element('.cb-button__text').click()
        browser.all('.cb-field__control')[0].type('first')
        browser.all('.cb-field__control')[1].type('last')
        browser.element('.cb-button__text').should(be.visible).click()
        browser.all('.cb-field__control')[0].type('first')
        browser.all('.cb-field__control')[1].type('last')
        browser.all('.cb-field__control')[2].type('address1')
        browser.all('.cb-field__control')[3].type('address2')
        browser.all('.cb-field__control')[4].type('city')
        browser.all('.cb-field__control')[5].type('zip')
        browser.all('.cb-field__control')[6].type('state')
        browser.element('[id="country"]').click().send_keys('Aland Islands')
        browser.element('.cb-button__text').click()
        browser.all('.cb-options__right')[0].click()
        browser.all('[class^=cb-field__control]')[0].click()
        browser.element('.cb-pmcard__title').click()
        browser.element('.cb-button__text').click()
        browser.all('.cb-bar__aside')[0].should(have.text('€1,694.00'))
        browser.all('.cb-bar__aside')[1].should(have.text('€504.00'))
        browser.element('.cb-subscribe__check').click()
        browser.element('.cb-button__text').click()
        browser.element(by.text('CLOSE')).should(be.visible).click().wait_until(be.visible)
        browser.driver.switch_to.default_content()
        time.sleep(10)
        return self

    def confirm_payment_no_e_with_extra_member(self):
        browser.element('.company-incorporation-success__btn').perform(command.js.scroll_into_view)
        browser.element('.company-incorporation-success-subtitle').should(have.text('€1694 Paid'))
        browser.element('.company-incorporation-success__btn').click()
        return self
