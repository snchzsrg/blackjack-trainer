'''
blackjack_sim.py
	a blackjack simulator

Written by Sergio Sanchez
'''

from deck import Deck
from hand import Hand
from dealer import Dealer
from player import Player
from strategy import *

def printHand(playerHand):
	print("\n")
	for card in playerHand.getHand():
		print(card)
	print("Value = %d\n" % playerHand.getValue())

# shuffle the deck
deck = Deck()
deck.shuffle()

# deal the cards
me = Player(deck.draw(),deck.draw())
dealer = Dealer(deck.draw(),deck.draw())

printHand(me.getHand())

if me.hasBlackjack():
	if dealer.hasBlackjack():
		print("Both you and dealer have blackjack... Push...")
	else:
		print("BLACKJACK!")
		exit()

print("Dealer shows %s" % dealer.openCardValue())

# play my hand
while True:

	if me.getHand().getValue() > 21:
		print("Bust! Dealer wins!")
		exit()  # dealer wins on player bust

	elif me.getHand().isPair():
		bestmove = basic_strategy_pair[dealer.openCardValue()][me.getHand().getHand()[0].getRank()]

	elif me.getHand().isSoft():
		bestmove = basic_strategy_soft[dealer.openCardValue()][me.getHand().getValue()-11]

	else:
		bestmove = basic_strategy_hard[dealer.openCardValue()][me.getHand().getValue()]

	print("My best move is %s" % BESTPLAY[bestmove])


	# Until logic for a split is put in, reevaluate as hard hand:
	if bestmove == SP:
		bestmove = basic_strategy_hard[dealer.openCardValue()][me.getHand().getValue()]


	if bestmove == H or bestmove == Dh or bestmove == Sh:
		print("Hit me!")
		me.hit(deck.draw())

	elif bestmove == S or bestmove == Ds:
		print("Stand!")
		break

	else:
		print("There's no reason to be here...")
		break

	printHand(me.getHand())


# play Dealer's hand
while True:

	printHand(dealer.getHand())

	if dealer.getHand().getValue() < 17:
		print("Dealer hits!")
		dealer.hit(deck.draw())

	elif dealer.getHand().getValue() <= 21:
		print("Dealer Stands!")
		break

	elif dealer.getHand().getValue() > 21:
		print("Dealer bust! You win!")
		exit() # player wins on dealer bust

	else:
		print("There's no reason to be here...")
		break

# compare hands
myHandVal = me.getHand().getValue()
dealerVal = dealer.getHand().getValue()
print("You: %d -- Dealer: %d" % (myHandVal, dealerVal))
if dealerVal > myHandVal:
	print("Dealer wins!")

elif dealerVal < myHandVal:
	print("You win!")

else:
	print("Push...")
