'''
	A few notations to consider in this program:
	The four suits (exactly as written): Clubs, Diamonds, Spades, Hearts
	The players are stored as objects. The player object contains the hand and the number of points.
	Order of suits:
	
	 
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
	hand = [];
	def __init__(self):
		self.points = 0;
		
	def setHand(self,hand):
		self.hand = hand;
		
	'''
		getHand method:
		parameter: none
		return: a list of integers, between 0 and 51 inclusive,
			of the cards in the player's hand 
	'''
	def getHand():
		return hand;

	
	
	'''
		playcard method
		parameter:  -list of cards played so far, 
						for the first player, the list will be empty
					-the current card the player wants to play
		return true if the card played is valid, false otherwise
		this is used for non-cpu players
		
	'''	
	def playCardUser(self, sofar, card):
		if(len(sofar) == 0):
			self.hand.remove(card);
			return true;
		else:
			leadingCard = sofar[0];
			lb = (leadingCard/13)*13;
			ub = lb + 12;
			valids = [];
			for i in range(len(hands)):
				if(hands[i] >= lb and hands[i] <= ub):
					valids.append(hands[i]);
			if(len(valids) == 0):
				self.hand.remove(card);
				return true;
			else:
				return false;
			
				
	'''
		playCardAuto method
		parameter: list of cards played so far
		return: the card to play (int between 0 and 51
		this method is only used for cpu players
		calls the AI method in the playCardAuto method
		
	'''
	def playCardAuto(self, sofar):
		return PlayCardAuto.playCard(self, sofar);
	
	def passCards():
		#more implementation
		return 0;
		
		
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
	'''				 
	for i in range(4):
		currhand = hands[i];
		a = currhand.sort();
		toAssign = {};
		toAssign['Spades']  =[];
		toAssign['Hearts']  =[];
		toAssign['Clubs']   =[];
		toAssign['Diamonds']=[];
		for j in currhand:
			suit = j/13;
			card = j%13;
			if(suit == 0):
				toAssign['Clubs'].append(card);
			if(suit == 1):
				toAssign['Diamonds'].append(card);
			if(suit == 2):
				toAssign['Spades'].append(card);
			if(suit == 3):
				toAssign['Hearts'].append(card);
		print toAssign
		playerList[i].setHand(toAssign);
	'''
a = Player();
b = Player();
c = Player();
d = Player();
Deal([a,b,c,d]);
for i in [a,b,c,d]:
	print i.hand;		





