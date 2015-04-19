#------------------------
#     MAIN GAME LOOP
#------------------------

import pygame, sys, random
from pygame.locals import *

from Graphics import *
import Graphics as graphics

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

def handleInput(hand,selection,state):
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
		graphics.displayCardPlay(hand.pop(selection),0)
		
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
		
	return (hand,selection,state)

#---------------------
#     START GAME!
#---------------------

#initialize graphics
initialize(windowwidth,windowheight,fps_limit)

#temporary hand for testing
hand = random.sample(range(0,52),13)

selection = 0
state = True
#game ends when state is False
while state:
	
	#display the player's hand with the current selection highlighted
	(hand,selection) = displayPlayerHand(hand,selection)
		
	#blit the frame to the display surface and update the game window
	graphics.displaysurf.blit(graphics.frame, (0,0))
	pygame.display.update()
	
	#refresh the frame
	graphics.frame.fill(background_color)
	
	#handle any user input
	(hand,selection,state) = handleInput(hand,selection,state)
	
	#wait for clock tick before next loop iteration
	fpsclock.tick(fps_limit)
