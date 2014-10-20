'''
dealer.py
	the dealer in blackjack

Written by Sergio Sanchez
'''

from player import Player

class Dealer(Player):

	def __init__(self, card_face_up, card_face_down, standOnSoft17=True):
		Player.__init__(self, card_face_up, card_face_down)
		self.openCard = card_face_up
		self.standOnSoft17 = standOnSoft17

	def openCardValue(self):
		return self.openCard.getRank()
