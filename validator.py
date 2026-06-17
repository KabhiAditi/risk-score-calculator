class Validator:

    REQUIRED_FIELDS = [

        "phone_events",

        "multiple_person_events",

        "face_missing_events",

        "looking_away_events",

        "head_pose_events"
    ]

    @staticmethod
    def validate(events):

        validated = {}

        for field in (
            Validator.REQUIRED_FIELDS
        ):

            value = events.get(
                field,
                0
            )

            if not isinstance(
                value,
                int
            ):
                raise ValueError(
                    f"{field} must be integer"
                )

            if value < 0:
                raise ValueError(
                    f"{field} cannot be negative"
                )

            validated[field] = value

        return validated