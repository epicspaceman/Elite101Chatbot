from random import choice

def location_question(name, responses, positive_responses, negative_responses):
  user_location = input(f"Where do you live, {name}? ")
  input(f"How do you like {user_location}? ")
  print(choice(responses))

def hobby_question(name, responses, positive_responses, negative_responses):
  user_hobby = input(f"Do you have any hobbies {name}? ")
  input(f"Do you enjoy {user_hobby}? ")
  print(choice(responses))

def user_age(name, responses, positive_responses, negative_responses):
  user_age = int(input(f"What's your age {name}? "))
  if user_age < 18:
    user_response = input("How's school going? ").lower()
    if user_response in positive_responses:
      print("That's good to hear!")
    elif user_response in negative_responses:
      print("I hope it gets better!")
    else:
      print("Cool!")
  elif user_age < 23:
    user_response = input("How's college going? ").lower()
    if user_response in positive_responses:
      print("That's good to hear!")
    elif user_response in negative_responses:
      print("I hope it gets better!")
    else:
      print("Cool!")
  elif user_age < 30:
    user_response = input("Do you have a job? ").lower()
    if user_response == 'yes':
      input("How do like your job?")
      print(choice(responses))
    elif user_response == 'no':
      print("I hope you get one soon!")
    else:
      print("Cool!")
  else:
    print(choice(responses))