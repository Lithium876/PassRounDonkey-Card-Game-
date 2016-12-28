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

	def showDeck(self):
		for card in self.cards:
			print(card)

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

	def __len__(self):
		return len(hand)
		
	def drawCard(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def showHand(self):
		for card in self.hand:
			print(card)

	def getHand(self):
		arr_cards_in_hand=[]
		for card in self.hand:
			arr_cards_in_hand.append(card.getCard())#create a list of lists here
		return arr_cards_in_hand #returns flatten list

	def checkHand(self,current_card):
		print("[+]%s needs a %s of any suit to play..."%(self.name, current_card[len(current_card)-2]))
		time.sleep(2)
		for card_in_hand in self.hand:
			card=card_in_hand.getCard().split(' ')
			if card[0] in current_card[len(current_card)-2]:
				return True
			else:
				return False

	def __repr__(self):
		return '%s'%(self)
