import random
import library_bot as lb

user_ID = int(input("Hi, I'm BookBot, here to help you navigate _____ Public Library! Please enter your library card ID\n"))

bot = lb.library_bot(user_ID)
bot.user_feeling()
bot.check_overdue()

def next_action():
  user_req = input("What would you like me to do? I can, check if you have any books overdue, find a library location, or find a book or author based on title or author. [Overdue | Location | Search]")
  if user_req == "Location":
    zip_code = input("Please enter your zip code")
    bot.find_location(zip_code)
  elif user_req == "Overdue":
    bot.check_overdue()
  elif user_req == "Search":
    query = input("Please enter a author or book title.")
    bot.find_book(query)

