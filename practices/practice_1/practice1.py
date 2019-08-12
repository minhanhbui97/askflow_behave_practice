number_of_sessions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number_of_stars = ['one', 'two', 'three', 'four', 'five']

session_list = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
star_list = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

number_of_sessions_str = [str(session_number) for session_number in session_list.values()]

number_of_stars_int = [int(star_number) for star_number in star_list.keys()]

print(number_of_sessions_str)
print(number_of_stars_int)

print("Original: I completed 2 sessions and I rated my expert five stars")
print("After conversion: I completed %s" % str(number_of_sessions_str[1]) + " sessions and I rated my expert %s" % str(number_of_stars_int[4]) + " stars")