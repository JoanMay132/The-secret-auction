import art 
import os
print(art.logo)
should_continue=True
data_values={}

def finding_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_money= bidding_record[bidder]
        if bid_money>highest_bid:
            highest_bid=bid_money
            winner=bidder
    print(f"The winner is {winner} with a bid of {bid_money}")

while should_continue:
    name=input("What is your name? ")
    bid_price=int(input("What is your bid price? $"))
    data_values[name]=bid_price
    asking=input("Are there other users who want to bid? Type 'yes' or 'no' ").lower()
    if asking=='yes':
        should_continue
        os.system('CLS')

    elif asking=='no':
        should_continue=False
        finding_highest_bidder(data_values)

    