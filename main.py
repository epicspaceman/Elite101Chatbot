import random
import functions as fn

generic_responses = ['That\'s so cool!', 'Interesting!', 'Really?']
negative_responses = ['bad', 'disappointing', 'depressing', 'sucks', 'i hate it']
positive_responses = ['good', 'i like it' ]
user_name = input("Hello, what\'s your name? ")
user_response = ''


functions = [fn.location_question, fn.hobby_question, fn.user_age]

while user_response != 'no':
  random.choice(functions)(user_name, generic_responses, positive_responses, negative_responses)
  user_response = input("Would you like to continue our chat? ")

