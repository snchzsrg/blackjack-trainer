'''
player.py
    a player in blackjack

Written by Sergio Sanchez
'''

from hand import Hand

class Player:

	def __init__(self,card1,card2):
		self.hand = Hand()
		self.hand.deal(card1,card2)
		self.blackjack = False

		if self.hand.getValue() == 21:
			self.blackjack = True

	def getHand(self):
		return self.hand

	def hit(self, card):
		self.hand.draw(card)

	def hasBlackjack(self):
		return self.blackjack

	def printHand(self):
		for card in self.hand:
			print(card)
		print("Value = %d\n" % self.hand.getValue())
