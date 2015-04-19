# Program to test a game of hearts.

import GamePlayMethods
import CardClass

from Auto import Automate

#create 4 players
player1 = GamePlayMethods.Player()
player2 = GamePlayMethods.Player()
player3 = GamePlayMethods.Player()
player4 = GamePlayMethods.Player()

#put the players into one list
Players = [player1, player2, player3, player4]

#Deal out the cards to all the players
GamePlayMethods.Deal(Players)

turn = 0
sofar = []
#Test each trick

for i in range(13):
	#check on the first hand only
	if (i == 0):
		for k in range(4):
			if Players[k].hasTwoOfClubs:
				turn = k
				break
	
	#check what has been played so far
	sofar = []
	point_total = 0
	#each person plays a card (and loops through turn)
	for m in range(4):
		print str(turn) +" " + str(Players[turn].hand)
		card = Players[turn].playCardAuto(sofar)
		sofar.append(card)
		turn = (turn+1) % 4
		point_total += CardClass.pointValue(card)
	turn = CardClass.winner(sofar) #indicate who wins the trick
	Players[turn].points += point_total

	print sofar


auto = Automate()
player = GamePlayMethods.Player()
hand = [1, 6, 10, 14, 29, 32, 39, 41, 42, 43, 45, 46, 47]
sofar = [0,2,11]
player.setHand(hand)
print auto.playCard(player, sofar)
