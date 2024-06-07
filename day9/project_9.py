from replit import clear
from art import logo
print(logo)
bids={}
bid_finish=False
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"name1": 123, "name2": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
while not bid_finish:
    name=input("what is your name ? ")
    price=int(input("what is your price  ? $"))
    bids[name]=price
    should_continue=input("Are there any other bidders ? type 'yes'or 'no'")
    if should_continue=="no":
        bid_finish=True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        clear()
        
        