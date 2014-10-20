'''
hand.py
	a hand in blackjack

Written by Sergio Sanchez
'''

class Hand:
	
	def __init__(self):
		self.hand = []
		self.value = 0
		self.softHand = False
		self.pair = False
		self.blackjack = False

	def deal(self,card1,card2):
		self.draw(card1)
		self.draw(card2)

		if self.hand[0].getRank() == self.hand[1].getRank():
			self.pair = True

		if self.value == 21:
			self.blackjack = True

	def draw(self,card):
		self.hand.append(card)
		self.value += card.blackjackValue()

		if card.getRank() == 'A' and self.value < 12:
			self.softHand = True
			self.value += 10     # evaluate with ace as 11

		if self.value > 21:
			if self.softHand:
				self.value -= 10
				self.softHand = False

	def getHand(self):
		return self.hand

	def getValue(self):
		return self.value

	def isSoft(self):
		return self.softHand

	def isPair(self):
		return self.pair

	def numCards(self):
		return len(self.hand)

	def isBlackjack(self):
		return self.blackjack