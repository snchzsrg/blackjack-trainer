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

# Define the possibile outcomes
WIN = 0
PUSH = WIN+1
LOSS = PUSH+1
BLKJK = LOSS+1


class BlackjackSimulator:

	def __init__(self,numOfRounds=1,numOfDecks=1):
		self.numOfRounds = numOfRounds
		self.numOfDecks = numOfDecks

		self.wins = 0
		self.pushes = 0
		self.losses = 0
		self.blackjacks = 0
		self.roundsPlayed = 0

		for _ in range(self.numOfRounds):

			result = 0

			if result == BLKJK:
				self.wins += 1
				self.blackjacks += 1

			elif result == WIN:
				self.wins += 1

			elif result == PUSH:
				self.pushes += 1

			elif result == LOSS:
				self.losses += 1

			else:
				print("INVALID RESULT -- %d" % result)
				exit()

			self.roundsPlayed += 1

	def results(self):
		# Print outcome
		print("Rounds:\t%d" % self.numOfRounds)
		print("  Wins:\t%d" % self.wins)
		print("Pushes:\t%d" % self.pushes)
		print("Losses:\t%d" % self.losses)
		print("    BJ:\t%d" % self.blackjacks)

	def getWins(self):
		return self.wins

	def getLosses(self):
		return self.losses

	def getPushes(self):
		return self.pushes

	def getBlackjacks(self):
		return self.blackjacks

	def getRoundsPlayed(self):
		return self.roundsPlayed





# shuffle the deck
deck = Deck()
deck.shuffle()

# deal the cards
me = Player(deck.draw(),deck.draw())
dealer = Dealer(deck.draw(),deck.draw())

me.printHand()

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

	me.printHand()


# play Dealer's hand
while True:

	dealer.printHand()

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
