'''
dealer.py
	the dealer in blackjack

Written by Sergio Sanchez
'''

from hand import Hand

class Dealer:

	def __init__(self, card_face_up, card_face_down):
		self.hand = Hand()
		self.hand.deal(card_face_up, card_face_down)
		self.openCard = card_face_up
		self.standOnSoft17 = True

	def openCardValue(self):
		return self.openCard.getRank()

	def getHand(self):
		return self.hand

	def getHandValue(self):
		return self.hand.getValue()

	def hit(self,card):
		self.hand.draw(card)

