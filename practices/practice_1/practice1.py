number_of_sessions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_of_stars = ['one', 'two', 'three', 'four', 'five']

session_list = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
star_list = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

number_of_sessions_str = [str(session_number) for session_number in session_list.values()]
number_of_sessions_int = [session_number for session_number in session_list.keys()]

number_of_stars_int = [star_number for star_number in star_list.values()]
number_of_stars_str = [str(star_number) for star_number in star_list.keys()]


def convert(sentence_text, no_of_sessions, no_of_stars):

    split_text = sentence_text.split(' ', 11)
    split_text[2] = str(number_of_sessions_str[number_of_sessions_int.index(no_of_sessions)])
    split_text[9] = str(number_of_stars_int[number_of_stars_str.index(no_of_stars)])
    return ' '.join(split_text)


text = "I completed 2 sessions and I rated my expert five stars"
ff = convert(text, 9, "five")
print(ff)
