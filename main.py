import random
import functions as fn

generic_responses = ['That\'s so cool!', 'Interesting!', 'Really?']
user_location = ''
user_hobby = ''
user_name = input("Hello, what\'s your name? ")
user_response = ''

functions = [fn.location_question, fn.hobby_question]

while user_response != 'no':
  random.choice(functions)(user_name, generic_responses)
  user_response = input("Would you like to continue our chat? ")
