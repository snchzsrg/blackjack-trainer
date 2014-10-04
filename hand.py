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

	def deal(self,card1,card2):
		self.draw(card1)
		self.draw(card2)

	def draw(self,card):
		self.hand.append(card)
		self.value += card.blackjackValue()

		if card.getRank() == 'Ace' and self.value < 12:
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
