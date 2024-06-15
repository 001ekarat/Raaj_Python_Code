from art import logo
print(logo)
bids = {}
bidding_finished = False

while not bidding_finished:
    name = input(f"what is your name?")
    price = input("what is your bid amount? $")
    bids[name] = price
    should_continue = input("are there any others ? Type 'Yes' or 'no' .")
    if should_continue == "no":
        bidding_finished = True