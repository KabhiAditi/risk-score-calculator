from calculator.risk_calculator import (
    RiskCalculator
)

from utils.validator import (
    Validator
)

TEST_CASES = [

    {
        "name":
            "No Violations",

        "events": {}
    },

    {
        "name":
            "Phone Detected",

        "events": {
            "phone_events": 1
        }
    },

    {
        "name":
            "Face Missing Multiple Times",

        "events": {
            "face_missing_events": 4
        }
    },

    {
        "name":
            "Medium Risk",

        "events": {

            "phone_events": 1,

            "face_missing_events": 2
        }
    },

    {
        "name":
            "High Risk",

        "events": {

            "phone_events": 2,

            "multiple_person_events": 1
        }
    }
]


for case in TEST_CASES:

    print(
        "\n====================="
    )

    print(case["name"])

    validated = (
        Validator.validate(
            case["events"]
        )
    )

    result = (
        RiskCalculator.calculate(
            validated
        )
    )

    print(result)