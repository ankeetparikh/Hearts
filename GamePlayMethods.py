'''
	A few notations to consider in this program:
	The four suits (exactly as written): Clubs, Diamonds, Spades, Hearts
	The players are stored as objects. The player object contains the hand and the number of points.
	
	 
'''
import random;
import CardClass;
import PlayCardAuto;
'''
class Card:
	#implement here
'''
class Player:
	points = 0;
	hasTwoOfClubs = false;
	hand = [];
	def __init__(self):
		self.points = 0;
		
	def setHand(self,hand):
		self.hand = hand;
		self.hasTwoOfClubs = false;
		if(self.hand[0] == 0)
			self.hasTwoOfClubs = true;
		
	'''
		getHand method:
		parameter: none
		return: a list of integers, between 0 and 51 inclusive,
			of the cards in the player's hand 
	'''
	def getHand(self):
		return self.hand;

	
	
	'''
		playcard method
		parameter:  -list of cards played so far, 
						for the first player, the list will be empty
					-the current card the player wants to play
		return true if the card played is valid, 
		false otherwise this is used for non-cpu players
		
	'''	
	def playCardUser(self, sofar, card):
		if(len(sofar) == 0):
			#test if the player has the two of clubs:
			if(self.count(0) == 1): 
				if(card == 0):
					return [true, ''];
				else:
					return [false, 'You must play the two of clubs on the first round.']
			else:
				self.hand.remove(card);
				return [true, ''];
		else:
			leadingCard = sofar[0];
			lb = (leadingCard/13)*13;
			ub = lb + 12;
			valids = [];
			for i in range(len(hands)):
				if(hands[i] >= lb and hands[i] <= ub):
					valids.append(hands[i]);
			if(len(valids) == 0): #if they have no cards of the leading suit
				self.hand.remove(card);
				return [true,''];
			else:
				if(valids.count(card) == 1): #if they have a card of the leading suit
					return [true, ''];
				else:
					return [false, 'You must play a card of suit:' + CardClass.suit(leadingCard)]
			
				
	'''
		passCards method:
		paramters: cards that the user wants to pass
		removes those cards from the hand
		
	'''
	def passCards(self, cardsToPass):
		for i in cardsToPass:
			self.hand.remove(i);
	'''
		playCardAuto method
		parameter: list of cards played so far
		return: the card to play (int between 0 and 51
		this method is only used for cpu players
		calls the AI method in the playCardAuto method
		
	'''
	def playCardAuto(self, sofar):
		return Auto.playCard(self, sofar);
		
	def passCardsAuto():
		return Auto.passCard(self)
	
	def addPassCards(self,passed);
		self.hand.append(passed);
		self.hand.sort();
		return 0;
	def addPoints(self, total):
		self.points+=total;		
		
	'''
	parameter: the list of player objects (length must be 4)
	return: void
	Changes the hand of each player in playerlist
	'''

def Deal(playerList):
	Deck = range(52);
	random.shuffle(Deck);
	p1,p2,p3,p4 = Deck[0:13], Deck[13:26], Deck[26:39], Deck[39:52];
	hands = [p1,p2,p3,p4];
	for i in range(4):
		hands[i].sort();
		playerList[i].setHand(hands[i]);
	
a = Player();
b = Player();
c = Player();
d = Player();
Deal([a,b,c,d]);
for i in [a,b,c,d]:
	print i.hand;		

players = [a,b,c,d];
sofar = [];
for i in range(4):
	sofar.append(PlayCardAuto.playCard());
	



















