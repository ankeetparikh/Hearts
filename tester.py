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

roundnumber = 0

while player1.points < 100 and player2.points < 100 and player3.points < 100 and player4.points < 100:
	roundnumber += 1	
	score = [0,0,0,0]

	#Deal out the cards to all the players
	GamePlayMethods.Deal(Players)

	'''
	player1.setHand(range(13))
	player2.setHand(range(13,26))
	player3.setHand(range(26,39))
	player4.setHand(range(39,52))
	'''

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
			#print str(turn) +" " + str(Players[turn].hand)
			card = Players[turn].playCardAuto(sofar)
			sofar.append(card)
			turn = (turn+1) % 4
			point_total += CardClass.pointValue(card)
		turn = CardClass.winner(sofar) #indicate who wins the trick
		score[turn] += point_total
		
		'''
		print sofar
		
		print "hand %d" % (i+1)
		for r in range(4):
			print "player %d: %d" % (r+1, score[r])
		'''
		
	#Someone shot the moon!
	if score.count(26) == 1:
		for k in range(4):
			score[k] = 26 - score[k]

	#Input scores to players
	for m in range(4):
		Players[m].points += score[m]

	print "scores for round %d" % roundnumber
	#Print scores out for each player
	for p in range(4):
		print "player %d: %d" % (p+1, Players[p].points)


#Print out the winner of the game!
win_index = 1
win_score = Players[0].points

for s in range(4):
	if Players[s].points < win_score:
		win_index = s + 1
		win_score = Players[s].points
		
print "Winner is player %d with %d points!" % (win_index, win_score)		
