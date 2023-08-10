import allure
from pages.registration_page import RegistrationPage
from pages.onboarding_page import Onboarding
from pages.company_information_page import CompanyInformationPage
from pages.members_incorporation_page import MembersPage
from pages.incorporation_plan_page import IncorporationPlanPage
from pages.company_service_page import CompanyServicePage
from pages.control_panel_page import ControlPanel
from allure_commons.types import Severity


class TestIncorporationNoE(
    RegistrationPage,
    Onboarding,
    CompanyInformationPage,
    MembersPage,
    IncorporationPlanPage,
    CompanyServicePage,
    ControlPanel,
):

    @allure.severity(Severity.CRITICAL)
    @allure.tag("dev")
    @allure.feature("Incorporation")
    def test_one_member(self, setup_browser):
        with allure.step("Открываем страницу сайнапа"):
            self.open()

        with allure.step("Регистрируем пользователя"):
            self.registration()

        with allure.step("Выбираем маркет Эстония"):
            self.choose_estonia()

        with allure.step("Выбираем инкорпорацию"):
            self.choose_incorporation()

        with allure.step("Выбираем без е-резиденства"):
            self.choose_not_have_eres()

        with allure.step("Начинаем инкорпорацию"):
            self.start_incorporation_no_e()

        with allure.step("Заполняем информацию о компании"):
            self.type_company_name()
            self.choose_main_field_of_activity()
            self.choose_activity_code()
            self.choose_phone_code()
            self.type_company_phone()
            self.type_information_about_company_activity()
            self.should_have_information(self.company.capital_without_e)
            self.go_to_next_step()

        with allure.step("Добавляем единственного мембера"):
            self.add_member_no_e()
            self.first_member_should_be_added()
            self.go_to_next_page()

        with allure.step("Проверяем тексты на странице оплаты"):
            self.should_have_texts_when_no_e()

        with allure.step("Выбираем план Стандарт"):
            self.choose_standard_plan()

        with allure.step("Оплачиваем в виджете чаржби"):
            self.pay_incorporation_no_e_in_chargebee()

        with allure.step("Подтверждаем оплату"):
            self.confirm_payment_no_e()

        with allure.step("Закрываем окно инкорпорации с комплаенсом"):
            self.close_complience()

        with allure.step("Разлогиниваемся"):
            self.logout()

    @allure.severity(Severity.NORMAL)
    @allure.tag("dev")
    @allure.feature("Incorporation")
    def test_change_type_to_e(self, setup_browser):
        with allure.step("Открываем страницу сайнапа"):
            self.open()

        with allure.step("Регистрируем пользователя"):
            self.registration()

        with allure.step("Выбираем маркет Эстония"):
            self.choose_estonia()

        with allure.step("Выбираем инкорпорацию"):
            self.choose_incorporation()

        with allure.step("Выбираем без е-резиденства"):
            self.choose_not_have_eres()

        with allure.step("Начинаем инкорпорацию"):
            self.start_incorporation_no_e()

        with allure.step("Заполняем информацию о компании"):
            self.type_company_name()
            self.choose_main_field_of_activity()
            self.choose_activity_code()
            self.choose_phone_code()
            self.type_company_phone()
            self.type_information_about_company_activity()
            # проверяем, заполнены ли поля
            self.should_have_information(self.company.capital_without_e)
            self.go_to_next_step()

        with allure.step("Добавляем мембера"):
            self.add_member_no_e()
            self.first_member_should_be_added()

        with allure.step("Меняем тип инкорпорации"):
            self.reset_application()
            self.choose_incorporation_with_e()

        with allure.step("Заполняем информацию о компании"):
            self.type_company_name()
            self.choose_main_field_of_activity()
            self.choose_activity_code()
            self.choose_phone_code()
            self.type_company_phone()
            self.type_information_about_company_activity()
            # проверяем, заполнены ли поля
            self.should_have_information(self.company.capital_with_e)
            self.go_to_next_step()

        with allure.step("Добавляем мембера"):
            self.add_member_with_e()
            self.first_member_should_be_added()
            self.go_to_next_page()

        with allure.step("Проверяем тексты на странице оплаты"):
            self.should_have_texts_when_e()

        with allure.step("Выбираем план Стандарт"):
            self.choose_standard_plan()

        with allure.step("Оплачиваем в виджете чаржби"):
            self.pay_incorporation_with_digital_id_in_chargebee()

        with allure.step("Подтверждаем оплату"):
            self.confirm_payment_with_digital_id()

        with allure.step("Закрываем окно инкорпорации с комплаенсом"):
            self.close_complience()

        with allure.step("Разлогиниваемся"):
            self.logout()

