from voluptuous import Schema, PREVENT_EXTRA, Any

user_plan_schema = Schema({
    "data": {
        "user": {
            "me": {
                "user": {
                    "activePlan": {
                        "billingPeriod": str,
                        "documents": int,
                        "haveControlPanel": bool,
                        "id": str,
                        "name": str,
                        "period": str,
                        "type": str
                    }
                }
            }
        }
    }
},
    extra=PREVENT_EXTRA,
    required=True)

user_login_schema = Schema(
    {
        "data": {
            "user": {
                "login": {
                    "user": {
                        "email": str
                    },
                    "sid": str
                }
            }
        }
    },
    extra=PREVENT_EXTRA,
    required=True)

plans_schema = Schema(
    {
        "data": {
            "getActivePlans": [{
                "name": str,
                "description": Any(str, None),
                "order": int,
                "haveTooltip": bool,
                "tooltipText": Any(str, None),
                "documentsPeriod": Any(str, None),
                "features": [
                    {
                        "featuresText": str,
                        "order": int
                    }
                ],
                "monthlyPrice": [
                    {
                        "docs": int,
                        "price": int,
                        "chargebeeId": str
                    }
                ],
                "yearlyPrice": [{
                    "docs": int,
                    "price": int,
                    "chargebeeId": str
                }]
            }]
        }
    }, extra=PREVENT_EXTRA,
    required=True)
