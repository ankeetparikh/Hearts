#------------------------
#     MAIN GAME LOOP
#------------------------

import pygame, sys, random
from pygame.locals import *

from Graphics import *
import Graphics as graphics

from GamePlayMethods import *
import GamePlayMethods as gpm

import CardClass

from Auto import Automate

# Some fundamental constants
windowwidth = 640
windowheight = 480
fps_limit = 60

#initialize the fpsclock to ensure loops don't exceed the fps limit
fpsclock = pygame.time.Clock()

#waits for user input and returns the pressed key
def wait():
    while True:
        fpsclock.tick(fps_limit)
        for event in pygame.event.get():
            #check for quit events
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            #check for keypress
            if event.type == KEYDOWN and event.key in controls:
                return event.key

def handleInput(hand,selection,state,play_made):
	# temporary value should throw error if unchanged
	card = 52 
	
	#wait for keypress
	keypress = wait()
	
	# check for QUIT events
	for event in pygame.event.get(QUIT): 
		#end the game
		state = False
	
	if keypress == K_ESCAPE:
		#end the game
		state = False
	
	if keypress == K_RETURN and len(hand)>0:
		#display player's played card
		card = hand.pop(selection)
		graphics.displayCardPlay(card,0)
		
		play_made = True
		
		#if we select the last card, we must decrement selection,
		#since the hand is now one card fewer
		if selection == len(hand):
			selection -= 1
		
	if keypress == K_LEFT and selection > 0:
		#move the selection left
		selection -= 1
		
	if keypress == K_RIGHT and selection < len(hand)-1:
		#move the selection right
		selection += 1
		
	return (hand,selection,state,play_made,card)
	
def playerTurn(hand,state):
	card = 52
	selection = 0
	play_made = False
	while not play_made:
		#refresh the overlay
		graphics.overlay.fill(background_color)
		
		if not state:
			break
			
		#display the player's hand with the current selection highlighted
		displayPlayerHand(hand,selection)
			
		#blit the frame to the display surface and update the game window
		graphics.frame.blit(graphics.overlay,(0,windowheight-100))
		graphics.displaysurf.blit(graphics.frame, (0,0))
		pygame.display.update()
		
		#handle any user input
		(hand,selection,state,play_made,card) = handleInput(hand,selection,state,play_made)
		
		#wait for clock tick before next loop iteration
		fpsclock.tick(fps_limit)
		
	return (hand,state,card)

#---------------------
#     START GAME!
#---------------------

#initialize graphics
initialize(windowwidth,windowheight,fps_limit)

players = []
for i in range(4):
	p = Player()
	players.append(p)

gpm.Deal(players)


#temporary hand for testing
hand = random.sample(range(0,52),13)

turn = 0

state = True
roundnumber = 0

while (players[0].points < 100 and players[1].points < 100 and players[2].points < 100 and players[3].points < 100) and state:
	roundnumber += 1	
	score = [0,0,0,0]
	
	gpm.Deal(players)

	turn = 0
	sofar = []
	#Test each trick
	for i in range(13):
		graphics.frame.fill(background_color)
		#check on the first hand only
		if (i == 0):
			for k in range(4):
				if players[k].hasTwoOfClubs:
					turn = k
					break
					
		#check what has been played so far
		sofar = [52,52,52,52]
		point_total = 0
		#each person plays a card (and loops through turn)
		for m in range(4):
			if m == 0:
				leader = turn
			#print str(turn) +" " + str(Players[turn].hand)
			if turn == 0:
				(players[0].hand,state,card) = playerTurn(players[0].hand,state)
				if not state:
					pygame.quit()
					sys.exit()
			else:
				card = players[turn].playCardAuto(sofar)
				graphics.displayCardPlay(card,turn)
			sofar[turn] = card
			turn = (turn+1) % 4
			point_total += CardClass.pointValue(card)
			graphics.displaysurf.blit(graphics.frame, (0,0))
			pygame.display.update()
			fpsclock.tick(1)
		turn = CardClass.winner(sofar,leader) #indicate who wins the trick
		score[turn] += point_total
		fpsclock.tick(1)
"""
		print "scorer for trick %d" % (i+1)
		#Print scores out for each player
		for p in range(4):
			print "player %d: %d" % (p+1, score[p])
"""		
	#Someone shot the moon!
	if score.count(26) == 1:
		for k in range(4):
			score[k] = 26 - score[k]

	#Input scores to players
	for m in range(4):
		players[m].points += score[m]
			
	print "scores for round %d" % roundnumber
	#Print scores out for each player
	for p in range(4):
		print "player %d: %d" % (p+1, players[p].points)

"""
#game ends when state is False
while state:
	
	#display the player's hand with the current selection highlighted
	displayPlayerHand(hand,selection)
		
	#blit the frame to the display surface and update the game window
	graphics.displaysurf.blit(graphics.frame, (0,0))
	pygame.display.update()
	
	#refresh the frame
	graphics.frame.fill(background_color)
	
	#handle any user input
	(hand,selection,state) = handleInput(hand,selection,state)
	
	#wait for clock tick before next loop iteration
	fpsclock.tick(fps_limit)
"""
