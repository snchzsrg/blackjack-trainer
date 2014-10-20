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

# RUNTIME OPTIONS
NUMBER_OF_DECKS = 6
NUMBER_OF_ROUNDS = 1000

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

			result = self.playRound()

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

	def playRound(self):
		# shuffle the decks
		deck = Deck(self.numOfDecks)
		deck.shuffle()

		# deal the cards
		me = Player(deck.draw(),deck.draw())
		dealer = Dealer(deck.draw(),deck.draw())

		# check for BLACKJACK!
		if me.hasBlackjack():
			if dealer.hasBlackjack():
				return PUSH
			else:
				return BLKJK

		# play my hand
		while True:

			handvalue = me.getHand().getValue()

			if handvalue > 21:
				return LOSS

			elif me.getHand().isPair():
				bestmove = basic_strategy_pair[dealer.openCardValue()][me.getHand().getHand()[0].getRank()]

			elif me.getHand().isSoft():
				bestmove = basic_strategy_soft[dealer.openCardValue()][handvalue-11]

			else:
				bestmove = basic_strategy_hard[dealer.openCardValue()][handvalue]


			# ULTRA NINJA HACK:
			#   until logic for a split is put in, reevaluate as a hard hand
			if bestmove == SP:
				if handvalue == 4: handvalue = 5
				bestmove = basic_strategy_hard[dealer.openCardValue()][handvalue]

			if bestmove == H or bestmove == Dh or bestmove == Sh:
				me.hit(deck.draw())

			elif bestmove == S or bestmove == Ds:
				break  # stand

			else:
				print("There's no reason to be here!")
				exit()

		# play dealer's hand
		while True:
			handvalue = dealer.getHand().getValue()

			if handvalue < 17:
				dealer.hit(deck.draw())

			elif handvalue <= 21:
				break  # stand

			elif handvalue > 21:
				return WIN  # dealer

			else:
				print("There's no reason to be here!")
				exit()

		# compare hands
		myValue = me.getHand().getValue()
		dealerValue = dealer.getHand().getValue()

		if dealerValue > myValue:
			return LOSS

		elif dealerValue < myValue:
			return WIN

		elif dealerValue == myValue:
			return PUSH

		else:
			print("There's no reason to be here!")
			exit()

def main(numOfRounds=1,numOfDecks=1):
	bjsim = BlackjackSimulator(numOfRounds,numOfDecks)
	bjsim.results()

if __name__ == "__main__":
	main(NUMBER_OF_ROUNDS,NUMBER_OF_DECKS)
