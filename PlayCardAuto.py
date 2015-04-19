from random import randint

class PlayCardAuto:
	def __init__(self):
		pass

	def playCard(Player,sofar):
		r = randint(0,len(Player.hand))
		if len(sofar) == 0:
			play = Player.hand(r)
			Player.hand.pop(r)
		elif len(sofar) > 0:
			lead_card = sofar(1)
			lead_suit = lead_card/13
			for i in Player.hand:
				if i/13 == lead_suit:
					play = i
					Player.hand.remove(i)
					break
			play = Player.hand(r)
			Player.hand.pop(r)
		
		return play


