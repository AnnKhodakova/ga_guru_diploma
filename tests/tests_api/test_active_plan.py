from pytest_voluptuous import S
from schemas.user import user_plan_schema
from queries.users import query_string_active_plan
import allure
from allure_commons.types import Severity


# юзер со стандартом в Нидерландах
@allure.severity(Severity.NORMAL)
@allure.tag("dev")
@allure.feature("User current plan")
def test_plan_schema(login_nl, dev_session):
    response = dev_session.post(json={'query': query_string_active_plan}, headers={'Enty-Auth': login_nl})
    assert S(user_plan_schema) == response.json()


@allure.severity(Severity.NORMAL)
@allure.tag("dev")
@allure.feature("User current plan")
def test_plan_id(login_nl, dev_session):
    response = dev_session.post(json={'query': query_string_active_plan}, headers={'Enty-Auth': login_nl})
    assert response.json()['data']['user']['me']['user']['activePlan']['id'] == 'standard-15-yearly-nl-2023'


@allure.severity(Severity.NORMAL)
@allure.tag("dev")
@allure.feature("User current plan")
def test_plan_period(login_nl, dev_session):
    response = dev_session.post(json={'query': query_string_active_plan}, headers={'Enty-Auth': login_nl})
    assert response.json()['data']['user']['me']['user']['activePlan']['period'] == 'QuarterlyAcc'
