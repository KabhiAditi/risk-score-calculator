from config import (
    EVENT_WEIGHTS,
    MAX_RISK_SCORE
)


class RiskCalculator:

    @staticmethod
    def calculate(events):

        score = 0

        breakdown = {}

        for event, weight in (
            EVENT_WEIGHTS.items()
        ):

            count = events.get(
                event,
                0
            )

            event_score = (
                count * weight
            )

            score += event_score

            breakdown[event] = {

                "count": count,

                "weight": weight,

                "event_score":
                    event_score
            }

        score = min(
            score,
            MAX_RISK_SCORE
        )

        level = (
            RiskCalculator
            .get_risk_level(score)
        )

        return {

            "risk_score": score,

            "risk_level": level,

            "event_breakdown":
                breakdown
        }

    @staticmethod
    def get_risk_level(score):

        if score < 30:
            return "LOW"

        elif score < 70:
            return "MEDIUM"

        return "HIGH"