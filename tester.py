# Program to test a game of hearts.

import GamePlayMethods

#create 4 players
player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()

#put the players into one list
Players = [player1, player2, player3, player4]

#Deal out the cards to all the players
Deal(Players)

turn = 0
#Test each trick
for i in range(13):
	#check on the first hand only
	if (i == 0):
		for k in range(3):
			if Players[k].hasTwoOfClubs:
				turn = k
				break
	else:
		#check what has been played so far
		sofar = []
		point_total = 0
		#each person plays a card (and loops through turn)
		for m in range(3):
			card = Players[turn].playCardAuto(sofar)
			sofar.append(card)
			turn += 1
			turn = turn % 4
			point_total += CardClass.pointValue(card)
		index = CardClass.winner(sofar)
		Players[index].points += point_total
