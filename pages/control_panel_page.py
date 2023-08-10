from selene import browser


class ControlPanel:
    def logout(self):
        browser.element('.user-link__icon').hover()
        browser.all('.dropdown-menu__item')[2].click()

    def close_complience(self):
        browser.all('.close-icon')[0].click()
