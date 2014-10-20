''' 
deck.py
	a deck made up of cards from at least one standard 52-card deck

Written by Sergio Sanchez
'''

import random
from collections import deque
from card import Card

Suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
Rank = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

class Deck:

	def __init__(self, numOfDecks=1):
		self.deck = deque([])
		for _ in range(numOfDecks):
			for suit in Suit:
				for rank in Rank:
					self.deck.append(Card(rank,suit))

	def shuffle(self):
		random.shuffle(self.deck)

	def draw(self):
		try:
			return self.deck.popleft()
		except IndexError:
			print("Uh-oh! No cards left in the draw pile!")
