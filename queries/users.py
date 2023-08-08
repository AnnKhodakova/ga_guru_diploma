from graphql_query import Query, Operation, Field, Variable, Argument

user = Query(
    name="user",
    fields=[Field(name="me", fields=[Field(name="user", fields=[Field(name="activePlan", fields=["id", "billingPeriod",
                                                                                                 "documents",
                                                                                                 "haveControlPanel",
                                                                                                 "name", "period",
                                                                                                 "type"])])])]
)

active_user_plan = Operation(type="query", name="activePlan", queries=[user])
query_string_active_plan = active_user_plan.render()

plans = Query(
    name="getActivePlans",
    fields=["name", "description", "order", "haveTooltip", "tooltipText", "documentsPeriod",
            Field(name="features", fields=["featuresText", "order"]),
            Field(name="monthlyPrice", fields=["docs", "price", "chargebeeId"]),
            Field(name="yearlyPrice", fields=["docs", "price", "chargebeeId"])])

active_plans = Operation(type="query", name="getActivePlans", queries=[plans])
query_string_plans = active_plans.render()

input_var = Variable(name="input", type="UserLoginInputType!")

user = Query(
    name="user",
    fields=[Field(name="login", arguments=[Argument(name="input", value=input_var)],
                  fields=[Field(name="user", fields=["email"]), "sid"])])

login = Operation(type="mutation", name="login", queries=[user], variables=[input_var])
query_string_login = login.render()

variables_login_nl = {
    "input": {
        "login": "hajilep891@randrai.com",
        "password": "EntyTest123"
    }
}

variables_login_est = {
    "input": {
        "login": "kokidit328@bitvoo.com",
        "password": "EntyTest123"
    }
}
variables_for_admin = {
    "input": {
        "login": "wonakot918@brandoza.com",
        "password": "EntyTest123"
    }
}

var = Variable(name="userId", type="String!")
user_from_adminka = Query(
    name="admin",
    fields=[Field(name="loginByUser", arguments=[Argument(name="userId", value=var)])]
)
login_from_adminka = Operation(type="mutation", name="loginByUser", queries=[user_from_adminka], variables=[var])
query_string_login_from_adminka = login_from_adminka.render()

variables_login_from_adminka = {
    "userId": "f765636d-7ae3-48fd-a21a-716060c27314"
}
