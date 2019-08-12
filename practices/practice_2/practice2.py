from practices.enums import Session
from practices.invalid_value_exception import InvalidValueException


class Step:

    def __init__(self, number_of_sessions: int, number_of_stars: str):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):
        session_list = Session.NUMBER_TO_TEXT_MAP

        star_list = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

        print("I completed %s" % str(
            session_list.get(self.number_of_sessions)) + " sessions and I rated my expert %s" % str(
            star_list.get(self.number_of_stars)) + " stars")
        if self.number_of_sessions not in session_list:
            raise InvalidValueException("Invalid number of sessions")
        elif self.number_of_stars not in star_list:
            raise InvalidValueException("Invalid number of stars")


ff = Step(79, "five")
ff.make_step()
