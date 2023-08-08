from pages.company_service_page import CompanyServicePage
from pages.registration_page import RegistrationPage
from pages.onboarding_page import Onboarding
from pages.control_panel_page import ControlPanel
import allure
from allure_commons.types import Severity


class TestTransferEst(RegistrationPage, Onboarding, CompanyServicePage, ControlPanel):
    @allure.severity(Severity.CRITICAL)
    @allure.tag("dev")
    @allure.feature("Transfer Estonia")
    def test_from_onboarding(self, setup_browser):
        with allure.step("Открываем страницу сайнапа"):
            self.open()

        with allure.step("Регистрируем пользователя"):
            self.registration()

        with allure.step("Выбираем маркет Эстония"):
            self.choose_estonia()

        with allure.step("Выбираем трансфер компании"):
            self.choose_transfer_est()

        with allure.step("Трансферим компанию"):
            self.company_transfer_est()
            self.confirm_transfer()

        with allure.step("Разлогиниваемся"):
            self.logout()

    @allure.severity(Severity.CRITICAL)
    @allure.tag("dev")
    @allure.feature("Transfer Estonia")
    def test_from_modalka(self, setup_browser):
        with allure.step("Открываем страницу сайнапа"):
            self.open()

        with allure.step("Регистрируем пользователя"):
            self.registration()

        with allure.step("Выбираем маркет Эстония"):
            self.choose_estonia()

        with allure.step("Выбираем трансфер компании"):
            self.choose_transfer_est()

        with allure.step("Закрываем онбординг"):
            self.skip_for_now()

        with allure.step("Кликаем на карточку company"):
            self.go_to_company()

        with allure.step("Трансферим компанию через модалку Add company"):
            self.find_company_name_modalka()

        with allure.step("Разлогиниваемся"):
            self.logout()

    @allure.severity(Severity.CRITICAL)
    @allure.tag("dev")
    @allure.feature("Transfer Estonia")
    def test_from_service(self, setup_browser):
        with allure.step("Открываем страницу сайнапа"):
            self.open()

        with allure.step("Регистрируем пользователя"):
            self.registration()

        with allure.step("Выбираем маркет Эстония"):
            self.choose_estonia()

        with allure.step("Выбираем трансфер компании"):
            self.choose_transfer_est()

        with allure.step("Закрываем онбординг"):
            self.skip_for_now()

        with allure.step("Переходим в сервис company через навигацию"):
            self.go_to_company_from_navigation()

        with allure.step("Трансферим компанию в сервисе company через разводящий экран"):
            self.choose_transfer()
            self.company_transfer_est()
            self.confirm_transfer_from_service()
