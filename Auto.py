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
			return Player.hand.pop(r)
		else:
			lead_card = sofar[0]
			lead_suit = lead_card/13
			options = []
			for i in Player.hand:
				if i/13 == lead_suit:
					options.append(i)
			if(len(options) > 0):		
				r = randint(0, len(options)-1)
				play = options[r];
				Player.hand.remove(play);
				return play
			else:
				r = randint(0, len(Player.hand)-1);
				play = Player.hand[r];
				Player.hand.remove(play);
				return play;
		
	def passCard(self, Player):
		a = Player.hand.pop()
		b = Player.hand.pop()
		c = Player.hand.pop()
		return [a,b,c]


