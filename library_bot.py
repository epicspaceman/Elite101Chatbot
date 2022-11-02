from random import choice

class library_bot:
  def __init__(self, user_ID):
    self.ID = user_ID
    self.responses = ['That\'s so cool!', 'Interesting!', 'Really?']
    self.positive = ['good', 'i like it']
    self.negative = ['bad', 'disappointing', 'depressing', 'sucks', 'i hate it']

  def __str__(self):
    return "test"

  def get_lists(self):
    self.userIDList = {5436:"Jim", 6765:"Greg"}
    self.userOverdue = {5436:True, 6765:False}
    self.locations = {"Main Branch":64348, "Elm Rd. Branch":64354, "Duck Ln. Branch":647321}
    self.book_list = {"Harry Potter":"J.K. Rowling", "The Hobbit":"J.R.R. Tolkein"}
    self.name = self.userIDList[self.ID]

  def check_overdue(self):
    if self.userOverdue[self.ID]:
      print("Before going any further please make action to return overdue books or pay a fee online if the book is lost. If you need help finding a nearby library, I can assist.")
      find_location(input("Please enter your zip code."))

  def find_location(self, zip_code):
    if zip_code in self.locations:
      print(f"We have a location near you, please visit our {self.locations[zip_code]}.")
    else:
      print("It doesn't look like we have any locations near you, try our main branch!")

  def find_book(self, query):
    if query in self.book_list:
      print(f"I found {book_list[query]}.")
    
  def user_feeling(self):
    user_response = input(f"Hi {self.name}, how are you feeling today?\n")
    if user_response in self.positive:
      print("That's good to hear!")
    elif user_response in self.negative:
      print("Don't worry, it'll get better! A good book always cheers me up!")
    else:
      print(choice(self.responses))
    user_response = input().lower()
    if user_response == "how are you?":
      print("I'm doing good! Thanks for asking!")
    else:
      print(choice(responses))