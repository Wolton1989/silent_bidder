    
import os
from art2 import logo

print(logo)

# Initialize an empty dictionary to store bids
bids = {}

# Set a flag to track if bidding is done
bidding_done = False

# Function to clear the console
def clear():
    # Check if the OS is Windows
    if os.name == 'nt':
        os.system('cls')
    # For other OSes (Linux, Mac)
    else:
        os.system('clear')

# Function to find the highest bidder
def get_the_highest_bidder(bidding_record):
    highest_bidder = 0
    winner = ""
    
    # Loop through each bidder's record   
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
            
    print(f"The winner is {winner} with a bid of {highest_bidder}")

# Main bidding loop
while not bidding_done:
    name = input("What is your name? ")
    price = int(input("How much would you like to bid? R"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Yes or No.\n")
    if should_continue.lower() == "no":
        bidding_done = True
        get_the_highest_bidder(bids)
    elif should_continue.lower() == "yes":
        clear()
