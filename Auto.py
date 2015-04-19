from random import *
from GamePlayMethods import *
class Automate:
	def __init__(self):
		pass

	def playCard(self, Player,sofar):
		r = randint(0,len(Player.hand)-1)
		if(Player.hand.count(0) == 1):
			Player.hand.remove(0);
			Player.hasTwoOfClubs = False;
			return 0;
		if len(sofar) == 0:
			if(heartsBroken):
				return Player.hand.pop(r)
			else:
				options = [];
				for i in Player.hand:
					if(i < 39)
						options.add(i);
				if(len(options) > 0):
					r = randint(0, len(options)-1)
					choice = options[r];
					options.remove[r];
					return choice;
				else:
					r = randint(0, len(Player.hand)):
					choice = options[r];
					options.remove(choice);
					return choice
		else:
			lead_card = sofar[0]
			lead_suit = lead_card/13
			options = []
			for i in Player.hand:
				if i/13 == lead_suit:
					options.append(i);
			if(len(options) > 0):		
				r = randint(0, len(options)-1)
				play = options[r];
				Player.hand.remove(play);
				return play
			else: # no cards of leading suit
				#if no clubs on first round, cannot play point card
				if(lead_card == 0):
					options = [];
					for i in range(len(Player.hand)):
						curr = Player.hand[i];
						#choose non-point cards
						if(curr/13 != 3 and curr != 36):
							options.append(curr);
					if(len(options) > 0):
						r = randint(0, len(options)-1);
						choice = options[r];
						Player.hand.remove(choice);
						return choice; 
					else: #Unlikely, but a player might have to play a point card on the first round
						choice = Player.hand[r];
						Player.hand.remove(choice);
						return choice;
				#otherwise
				choice = Player.hand[r];
				Player.hand.remove(choice);
				return choice;
						
					
		
	def passCard(self, Player): #Pass the three highest hearts...
		container = sample(range(13),3)
		a = Player.hand.pop(container[0])
		b = Player.hand.pop(container[1])
		c = Player.hand.pop(container[2])
		return [a,b,c]
