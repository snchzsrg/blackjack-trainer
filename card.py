'''
card.py
    a card in a standard 52-card deck

Written by Sergio Sanchez
'''

class Card:

	 def __init__(self, rank, suit):
	 	self.rank = rank
	 	self.suit = suit

	 def getRank(self):
	 	return self.rank

	 def getSuit(self):
	 	return self.suit

	 def blackjackValue(self):
	 	if self.rank == 'Ace':
	 		return 1
	 	elif self.rank == 'Jack' or self.rank == 'Queen' or self.rank == 'King':
	 		return 10
	 	else:
	 		return int(self.rank)

	 def __str__(self):
	 	return("{0} of {1}".format(self.rank, self.suit))
