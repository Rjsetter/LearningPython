#_*_ encoding:utf-8_*_

import random
class Card(object):
	suit_names = ['Clubs','Diamonds', 'Hearts', 'Spades']#花色
	rank_name = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
	'Jack', 'Queen', 'King']#牌值

	def __init__(self, suit = 0, rank = 2):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return '%s of %s'%(	Card.rank_name[self.rank], 
		                   Card.suit_names[self.suit])

	def __lt__(self, other):
		"""利用元组进行比较大小，先比较第一个，在接着往后比较"""
		t1 = self.suit, self.rank
		t2 = other.suit, other.rank
		return t1 < t2

class Deck(object):
	def __init__(self):
		"""初始化牌组"""
		self.cards = []
		for suit in range(4):
			for rank in range(1, 14):
				card = Card(suit, rank)
				self.cards.append(str(card))

	def __str__(self):
		res = []
		for card in self.cards:
			res.append(card)
		return '\n'.join(res)

	def pop_card(self):
		return self.cards.pop()

	def add_card(self,card):
		self.cards.append(card)

	def shuffle(self):
		random.shuffle(self.cards)





deck =Deck()
print(deck)
deck.shuffle()
print(deck)

# card1 = card(2, 11)
# card2 = card(2, 9)
# print(card1)
# print(card2<card1) 