import random, time

class Card:
	def __init__(self, value):
		self.value = value

	def getCard(self):
		return "%s"%(self.value)

class Deck:
	def __init__(self):
		self.cards = []
		self.buildDeck()

	def buildDeck(self):
		for _ in range(0,4):
			for value in range(1, 14):
				if value == 1:
					self.cards.append(Card("Ace"))
				elif value == 11:
					self.cards.append(Card("Jack"))
				elif value == 12:
					self.cards.append(Card("Queen"))
				elif value == 13:
					self.cards.append(Card("King"))
				else:
					pass

	def shuffleDeck(self):
	#Fisher-Yates shuffle 
		for i in range (len(self.cards) -1,0,-1):
			rand = random.randint(0,i)
			self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

	def drawCard(self):
		return self.cards.pop()

	def __len__(self):
		return len(self.cards)

class Player:
	house =[]
	def __init__(self, name):
		self.name = name
		self.hand = []

	def drawCard(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def getHand(self):
		arr_cards_in_hand=[]
		for card in self.hand:
			arr_cards_in_hand.append(card.getCard())
		return arr_cards_in_hand