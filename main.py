from calculator.risk_calculator import (
    RiskCalculator
)

from utils.validator import (
    Validator
)


events = {

    "phone_events": 2,

    "multiple_person_events": 1,

    "face_missing_events": 3,

    "looking_away_events": 4,

    "head_pose_events": 1
}

validated_events = (
    Validator.validate(events)
)

result = (
    RiskCalculator.calculate(
        validated_events
    )
)

print("\n===== RISK REPORT =====")

print(
    f"Risk Score : "
    f"{result['risk_score']}"
)

print(
    f"Risk Level : "
    f"{result['risk_level']}"
)

print("\nEvent Breakdown:\n")

for event, details in (
    result["event_breakdown"]
    .items()
):

    print(
        f"{event}"
        f" -> Count={details['count']}"
        f", Weight={details['weight']}"
        f", Score={details['event_score']}"
    )