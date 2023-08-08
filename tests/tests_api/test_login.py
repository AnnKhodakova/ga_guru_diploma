from queries.users import query_string_login, query_string_login_from_adminka, variables_login_from_adminka, \
    variables_login_est, variables_login_nl
from schemas.user import user_login_schema
from pytest_voluptuous import S
import allure
from allure_commons.types import Severity


@allure.severity(Severity.NORMAL)
@allure.tag("dev")
@allure.feature("Login")
def test_login_schema(dev_session):
    response = dev_session.post(json={'query': query_string_login, 'variables': variables_login_est})
    assert S(user_login_schema) == response.json()


@allure.severity(Severity.CRITICAL)
@allure.tag("dev")
@allure.feature("Login")
def test_login_nl(dev_session):
    response = dev_session.post(json={'query': query_string_login, 'variables': variables_login_nl})
    token = response.json()['data']['user']['login']['sid']
    return token


@allure.severity(Severity.CRITICAL)
@allure.tag("dev")
@allure.feature("Login")
def test_login_est(dev_session):
    response = dev_session.post(json={'query': query_string_login, 'variables': variables_login_est})
    token = response.json()['data']['user']['login']['sid']
    return token


@allure.severity(Severity.CRITICAL)
@allure.tag("dev")
@allure.feature("Login")
def test_login_from_adminka(login_as_admin, dev_session):
    response = dev_session.post(json={'query': query_string_login_from_adminka,
                                      'variables': variables_login_from_adminka},
                                headers={'Enty-Auth': login_as_admin}
                                )
    assert response.json()['data']['admin']['loginByUser'] is True
