class EventModel:

    def __init__(
        self,
        phone_events=0,
        multiple_person_events=0,
        face_missing_events=0,
        looking_away_events=0,
        head_pose_events=0
    ):

        self.phone_events = phone_events

        self.multiple_person_events = (
            multiple_person_events
        )

        self.face_missing_events = (
            face_missing_events
        )

        self.looking_away_events = (
            looking_away_events
        )

        self.head_pose_events = (
            head_pose_events
        )

    def to_dict(self):

        return {

            "phone_events":
                self.phone_events,

            "multiple_person_events":
                self.multiple_person_events,

            "face_missing_events":
                self.face_missing_events,

            "looking_away_events":
                self.looking_away_events,

            "head_pose_events":
                self.head_pose_events
        }