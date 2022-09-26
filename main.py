from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print(f'Welcome to the secret auction program.\n')

name = input('What is your name? ')
bid = input('What is your bid? $')

name_dictionary = {}

def add_name(name_bidder, bid_amount):
  name_dictionary[name_bidder] = bid_amount

add_name(name, bid)

other_bid = input(f"Are there any other bidders? Type 'yes' or 'no'.")

while other_bid == 'yes':
  clear()
  name = input('What is your name? ')
  bid = input('What is your bid? $')
  add_name(name,bid)
  other_bid = input(f"Are there any other bidders? Type 'yes' or 'no'.")
 
else:
  find_max = max(name_dictionary, key=name_dictionary.get)
  print(f'The winner is {find_max} with a bid of ${name_dictionary[find_max]}')

#print(name_dictionary)
  
