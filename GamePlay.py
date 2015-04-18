'''
	A few notations to consider in this program:
	The four suits: spades, hearts, diamonds and clubs are always going to be lowercase
	The players are stored as objects. The player object contains the hand and the number of points.
	 
'''
import random;

Deck = [];

class Player:
	points = 0;
	clubs = [];
	spades = [];
	diamonds = [];
	hearts = [];
	def __init__(self, hand):
		self.points = 0;
		self.setHand(hand);
		
	def setHand(hand):
		self.clubs = hand['clubs'];
		self.hearts = hand['hearts'];
		self.spades = hand['spades'];
		self.hearts = hand['hearts'];
			
	def playCard():
		#implementation goes here
	def pass():
		#more implementation

def Deal():
	
					 
	
print Deck;