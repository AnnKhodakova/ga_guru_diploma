from pages.control_panel_page import ControlPanel
from pages.registration_page import RegistrationPage
from pages.onboarding_page import Onboarding
from pages.company_service_page import CompanyServicePage
import allure
from allure_commons.types import Severity


class TestIncorporationNl(RegistrationPage, Onboarding, CompanyServicePage, ControlPanel):
    @allure.severity(Severity.CRITICAL)
    @allure.tag("dev")
    @allure.feature("Incorporation")
    def test_from_onboarding(self, setup_browser):
        with allure.step("Открываем страницу сайнапа"):
            self.open()

        with allure.step("Регистрируем пользователя"):
            self.registration()

        with allure.step("Выбираем маркет Нидерланды"):
            self.choose_netherlands()

        with allure.step("Запрашиваем инкорпорацию в Нидерландах"):
            self.request_incorporation_nl()

        with allure.step("Разлогиниваемся"):
            self.logout()

    @allure.severity(Severity.CRITICAL)
    @allure.tag("dev")
    @allure.feature("Incorporation")
    def test_from_company(self, setup_browser):
        with allure.step("Открываем страницу сайнапа"):
            self.open()

        with allure.step("Регистрируем пользователя"):
            self.registration()

        with allure.step("Выбираем маркет Нидерланды"):
            self.choose_netherlands()

        with allure.step("Закрываем онбординг"):
            self.skip_for_now()

        with allure.step("Переходим в сервис company через навигацию"):
            self.go_to_company_from_navigation()

        with allure.step("Трансферим компанию через разводящий экран"):
            self.choose_transfer()
            self.request_incorporation_nl()

        with allure.step("Разлогиниваемся"):
            self.logout()
