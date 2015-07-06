def advanced_join_strings(list_of_words):
    string_of_words = ", ".join(list_of_words)    
    return string_of_words


my_list = ["Labrador"]

advanced_join_strings(my_list)

#    if len(list_of_words) == 0:
#        return list_of_words[0]
#    else:
#        for word in list_of_words:
#        output_string = output_string + ", %s" % word

#     """Return a single string with each word from the input list
#     separated by a comma.
#
#         >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
#         'Labrador, Poodle, French Bulldog'
#
#     If there's only one thing in the list, it should return just that
#     thing, of course:
#
#         >>> advanced_join_strings(["Pretzel"])
#         'Pretzel'
#
#     """
#
#     return ""