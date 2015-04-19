def suit(card):	
		check_suit = card/13
		if check_suit == 0:
			return "Clubs"
		elif check_suit == 1:
			return "Diamonds"
		elif check_suit == 2:
			return "Spades"
		elif check_suit == 3:
			return "Hearts"

def value(card):
		check_value = card%13
		if check_value <= 9:
			return str(check_value + 2)
		elif check_value == 10:
			return "Jack"
		elif check_value == 11:
			return "Queen"
		elif check_value == 12:
			return "King"
		elif check_value == 13:
			return "Ace"

def name_of_card(card):
		return value(card) + " of " + suit(card)


class Card:
	def __init__(self,card1,card2,card3,card4):
		self.card1 = card1
		self.card2 = card2
		self.card3 = card3
		self.card4 = card4

	def winner(self):
		cards = [self.card2,self.card3,self.card4]
		win = 0
		for i in cards:
			if suit(i) == suit(self.card1):
				if value(i) > value(self.card1):
					win = cards.index(i) + 1

		return win 