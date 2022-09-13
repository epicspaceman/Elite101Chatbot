import random

def location_question(name, responses):
  user_location = input(f"Where do you live, {name}? ")
  input(f"How do you like {user_location}? ")
  print(random.choice(responses))

def hobby_question(name, responses):
  user_hobby = input(f"Do you have any hobbies {name}? ")
  input(f"Do you enjoy {user_hobby}? ")
  print(random.choice(responses))
  