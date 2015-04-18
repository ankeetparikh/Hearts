'''
	A few notations to consider in this program:
	The four suits: spades, hearts, diamonds and clubs are always going to be lowercase
	The players are stored as objects. The player object contains the hand and the number of points.
	Order of suits:
	
	 
'''
import random;

'''
class Card:
	#implement here
'''
class Player:
	points = 0;
	clubs = [];
	diamonds = [];
	spades = []
	hearts = [];
	def __init__(self):
		self.points = 0;
		
	def setHand(self,hand):
		self.clubs = hand['clubs'];
		self.diamonds = hand['diamonds'];
		self.spades = hand['spades'];
		self.hearts = hand['hearts'];
	'''		
	def playCard():
		#implementation goes here
	def pass():
		#more implementation
	'''
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
		currhand = hands[i];
		a = currhand.sort();
		toAssign = {};
		toAssign['spades']  =[];
		toAssign['hearts']  =[];
		toAssign['clubs']   =[];
		toAssign['diamonds']=[];
		for j in currhand:
			suit = j/13;
			card = j%13;
			if(suit == 0):
				toAssign['clubs'].append(card);
			if(suit == 1):
				toAssign['diamonds'].append(card);
			if(suit == 2):
				toAssign['spades'].append(card);
			if(suit == 3):
				toAssign['hearts'].append(card);
		print toAssign
		playerList[i].setHand(toAssign);
a = Player();
b = Player();
c = Player();
d = Player();
Deal([a,b,c,d]);		





