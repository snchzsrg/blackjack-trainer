'''
blackjack_sim.py
	a simple simulator that
	  - shuffles the deck
	  - deals a hand
	  - hits, stays, or busts based on the hand value

Written by Sergio Sanchez
'''

from deck import Deck
from hand import Hand
from dealer import Dealer

def printHand(hand):
	print("\n")
	for card in hand.getHand():
		print(card)
	print("Value = %d\n" % hand.getValue())

# shuffle the deck
deck = Deck().shuffled()

# deal the cards
myHand = Hand()
myHand.deal(deck.popleft(),deck.popleft())
dealer = Dealer(deck.popleft(),deck.popleft())

# play my hand
while True:

	printHand(myHand)

	if myHand.getValue() < 17:
		print("Hit me!")
		myHand.draw(deck.popleft())

	elif myHand.getValue() <= 21:
		print("Stay!")
		break

	elif myHand.getValue() > 21:
		print("Bust! Dealer wins!")
		exit()  # dealer wins on player bust

# play Dealer's hand
while True:

	printHand(dealer.getHand())

	if dealer.getHand().getValue() < 17:
		print("Dealer hits!")
		dealer.hit(deck.popleft())

	elif dealer.getHand().getValue() <= 21:
		print("Dealer stays!")
		break

	elif dealer.getHand().getValue() > 21:
		print("Dealer bust! You win!")
		exit() # player wins on dealer bust

# compare hands
myHandVal = myHand.getValue()
dealerVal = dealer.getHandValue()
print("You: %d -- Dealer: %d" % (myHandVal, dealerVal))
if dealerVal > myHandVal:
	print("Dealer wins!")

elif dealerVal < myHandVal:
	print("You win!")

else:
	print("Push...")
