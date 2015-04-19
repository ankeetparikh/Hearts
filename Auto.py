from random import randint

class Auto:
	def __init__(self):
		pass

	def playCard(Player,sofar):
		r = randint(0,len(Player.hand))
		if len(sofar) == 0:
			play = Player.hand(r)
			Player.hand.pop(r)
		elif len(sofar) > 0:
			lead_card = sofar[0]
			lead_suit = lead_card/13
			for i in Player.hand:
				options = []
				if i/13 == lead_suit:
					options.append(i)
				if len(options)>0:
					play = options[randint(0,len(options)-1)]
					Player.hand.remove(play)
			play = Player.hand(r)
			Player.hand.pop(r)
		
		return play

	def passCard(Player):
		a = Player.hand.pop()
		b = Player.hand.pop()
		c = Player.hand.pop()
		return [a,b,c]


