from practices.practice_2.enums import Session
from practices.practice_2.invalid_value_exception import InvalidValueException


class Step:

    text = "I completed x_as_int sessions and I rated my expert y_as_text stars"

    def __init__(self, number_of_sessions, number_of_stars):
        self.number_of_sessions = number_of_sessions
        self.number_of_stars = number_of_stars

    def make_step(self):
        session_list = Session.NUMBER_TO_TEXT_MAP
        star_list = Session.TEXT_TO_NUMBER_MAP

        number_of_sessions_str = [str(session_number) for session_number in session_list.values()]
        number_of_sessions_int = [session_number for session_number in session_list.keys()]

        number_of_stars_int = [star_number for star_number in star_list.values()]
        number_of_stars_str = [str(star_number) for star_number in star_list.keys()]

        split_text = self.text.split(' ', 11)

        try:
            split_text[2] = str(number_of_sessions_str[number_of_sessions_int.index(self.number_of_sessions)])
        except ValueError:
            raise InvalidValueException("Invalid number of sessions: " + str(self.number_of_sessions))
        try:
            split_text[9] = str(number_of_stars_int[number_of_stars_str.index(self.number_of_stars)])
        except ValueError:
            raise InvalidValueException("Invalid number of stars: " + str(self.number_of_stars))

        return ' '.join(split_text)
