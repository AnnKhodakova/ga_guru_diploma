from pytest_voluptuous import S
from queries.users import query_string_plans
from schemas.user import plans_schema
import allure
from allure_commons.types import Severity


@allure.severity(Severity.CRITICAL)
@allure.tag("dev")
@allure.feature("Pricing")
def test_get_plans_for_user_schema(login_nl, dev_session):
    response = dev_session.post(json={'query': query_string_plans}, headers={'Enty-Auth': login_nl})
    assert S(plans_schema) == response.json()


@allure.severity(Severity.CRITICAL)
@allure.tag("dev")
@allure.feature("Pricing")
def test_plans_for_est_user(login_est, dev_session):
    response = dev_session.post(json={'query': query_string_plans}, headers={'Enty-Auth': login_est})
    assert response.json()['data']['getActivePlans'][4]['name'] == 'E-com'


@allure.severity(Severity.CRITICAL)
@allure.tag("dev")
@allure.feature("Pricing")
def test_plans_for_nl_user(login_nl, dev_session):
    response = dev_session.post(json={'query': query_string_plans}, headers={'Enty-Auth': login_nl})
    assert response.json()['data']['getActivePlans'][2][
               'description'] == 'Delegeer BTW kwartaal rapportage voor ZZP, BV en VOF aan Enty'


@allure.severity(Severity.NORMAL)
@allure.tag("dev")
@allure.feature("Pricing")
def test_documents_type_in_standard_plan_nl(login_nl, dev_session):
    response = dev_session.post(json={'query': query_string_plans}, headers={'Enty-Auth': login_nl})
    assert response.json()['data']['getActivePlans'][2]['documentsPeriod'] == 'quarterlyacc'


@allure.severity(Severity.NORMAL)
@allure.tag("dev")
@allure.feature("Pricing")
def test_documents_type_in_standard_plan_est(login_est, dev_session):
    response = dev_session.post(json={'query': query_string_plans}, headers={'Enty-Auth': login_est})
    assert response.json()['data']['getActivePlans'][2]['documentsPeriod'] == 'yearlyacc'
