import art
# TODO-1: Ask the user for input
bidders = {}
bidding_over = False
max_bidding = 0
winner = ""
print(art.logo)
print("Welcome to the mini Auction\n")

while(bidding_over == False):
    bidder_name = input("Enter your name\n")
    bidder_amt = input("Enter your Bidding Amt $")
    bidders[bidder_name] = bidder_amt

    temp = input("Are there any more bidders?").lower()
    if temp == "no":
        bidding_over = True
    else:
        print("\n" * 80)

for bidder in bidders:

    int_amt = int(bidders[bidder])
    if int_amt > max_bidding:
        max_bidding = int_amt
        winner = bidder

print(f"Winner of Mini Auction is {winner} with a whopping bid of ${max_bidding}")

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


