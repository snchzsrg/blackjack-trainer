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
	 	if self.rank == 'A':
	 		return 1
	 	elif self.rank == 'T' or self.rank == 'J' or self.rank == 'Q' or self.rank == 'K':
	 		return 10
	 	else:
	 		return int(self.rank)

	 def __str__(self):
	 	return("{0} of {1}".format(self.rank, self.suit))
