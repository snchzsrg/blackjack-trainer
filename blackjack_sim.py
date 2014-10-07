'''
blackjack_sim.py
	a blackjack simulator

Written by Sergio Sanchez
'''

from deck import Deck
from hand import Hand
from dealer import Dealer
from strategy import *

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

printHand(myHand)

if myHand.isBlackjack():
	if dealer.isBlackjack():
		print("Both you and dealer have blackjack... Push...")
	else:
		print("BLACKJACK!")
		exit()

print("Dealer shows %s" % dealer.openCardValue())

# play my hand
while True:

	if myHand.getValue() > 21:
		print("Bust! Dealer wins!")
		exit()  # dealer wins on player bust

	elif myHand.isPair() and len(myHand.getHand()) == 2:
		bestmove = basic_strategy_pair[dealer.openCardValue()][myHand.getHand()[0].getRank()]

	elif myHand.isSoft():
		bestmove = basic_strategy_soft[dealer.openCardValue()][myHand.getValue()-11]

	else:
		bestmove = basic_strategy_hard[dealer.openCardValue()][myHand.getValue()]

	print("My best move is %s" % BESTPLAY[bestmove])


	if bestmove == H or bestmove == Dh or bestmove == Sh:
		print("Hit me!")
		myHand.draw(deck.popleft())

	elif bestmove == S or bestmove == Ds:
		print("Stand!")
		break

	printHand(myHand)


# play Dealer's hand
while True:

	printHand(dealer.getHand())

	if dealer.getHand().getValue() < 17:
		print("Dealer hits!")
		dealer.hit(deck.popleft())

	elif dealer.getHand().getValue() <= 21:
		print("Dealer Stands!")
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
