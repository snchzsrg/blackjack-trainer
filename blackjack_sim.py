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

def printHand(hand):
	print("\n")
	for card in hand.getHand():
		print(card)
	print("Value = %d\n" % hand.getValue())

deck = Deck().shuffled()
hand = Hand()

hand.deal(deck.popleft(),deck.popleft())

while True:

	printHand(hand)

	if hand.getValue() < 17:
		print("Hit me!")
		hand.draw(deck.popleft())

	elif hand.getValue() <= 21:
		print("Stay!")
		break

	elif hand.getValue() > 21:
		print("Bust!")
		break
