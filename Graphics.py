#--------------------------
#     GRAPHICS LIBRARY
#--------------------------

import pygame, sys, random
from pygame.locals import *
	
# RGB code reference
WHITE = (250,250,250)
DARK_GREEN = (0,150,0)
BLACK = (0,0,0)
RED = (250,0,0)
LIGHT_GREY =    (200,200,200)

# Aesthetics
background_color = DARK_GREEN
text_color = WHITE
font_size = 10
large_font_size = 20

# list of keybindings
controls = [
	K_ESCAPE, 	#exit
	K_RETURN, 	#play card
	K_LEFT,		#move selection left 
	K_RIGHT		#move selection right
]

# Card number key
card_dict = {
	0:'2',
	1:'3',
	2:'4',
	3:'5',
	4:'6',
	5:'7',
	6:'8',
	7:'9',
	8:'10',
	9:'J',
	10:'Q',
	11:'K',
	12:'A'}



# returns a surface with the graphic of a given card
def getCardFace(card_num,card_background_color,number_font,width,height):
	global card_dict

	suit = card_num/13
	number = card_dict[card_num%13]
	
	#instantiate a surface with given width and height
	card = pygame.Surface((width,height))
	#fill the card surface with the given background color
	card.fill(card_background_color)
	
	#set the correct color and suit asset for the card
	if suit == 0: 
		card_color = BLACK
		suit_img = pygame.image.load('club.png')
	elif suit == 1: 
		card_color = RED
		suit_img = pygame.image.load('diamond.png')
	elif suit == 2:
		card_color = BLACK
		suit_img = pygame.image.load('spade.png')
	elif suit == 3:
		card_color = RED
		suit_img = pygame.image.load('heart.png')
	
	#this conversion makes sure the .png's transparency is preserved
	suit_img = suit_img.convert_alpha()
	#create a surface with the card number
	numberlabel = number_font.render(number, True, card_color, card_background_color)
	
	#blit the number to the top-left and bottom-right corners
	card.blit(numberlabel, (2,2))
	card.blit(pygame.transform.rotate(numberlabel,180), 
		(width-2-number_font.size(number)[0],
		height-2-number_font.size(number)[1]))
	#blit the suit asset to the center of the card surface
	card.blit(suit_img,((width-20)/2,(height-20)/2))
	
	return card
	
#displays the hand of the player across the bottom of the screen
def displayPlayerHand(hand,selection):
	for i in range(0,len(hand)):
		#distinguish the currently selected card from the rest
		if i == selection:
			card_color = WHITE
			offset = -5
		else:
			card_color = LIGHT_GREY
			offset = 0
		#create a surface for the ith card in the player's hand
		card = getCardFace(hand[i],card_color,basicfont,40,60)
		#blit the card to the display surface with dynamic centering
		overlay.blit(card,((windowwidth-45*len(hand))/2+i*45, 100-65+offset))

#display card played from given side
def displayCardPlay(card_num,side):
	card = getCardFace(card_num,WHITE,largefont,80,120);
	#rotate the card as needed, and blit it at the correct location
	card = pygame.transform.rotate(card,((4-side)%4)*90)
	if side == 0:
		location = ((windowwidth-80)/2,(windowheight-430)/2+210)
	if side == 1:
		location = ((windowwidth-330)/2,(windowheight-100)/2-40)
	if side == 2:
		location = ((windowwidth-80)/2,(windowheight-430)/2)
	if side == 3:
		location = ((windowwidth-330)/2+210,(windowheight-100)/2-40)
	frame.blit(card,location)

#initialize some base graphics elements
def initialize(gamewidth,gameheight,fps_limit):
    global displaysurf,basicfont,largefont,frame,overlay
    global windowwidth,windowheight,fps
    
    windowwidth = gamewidth
    windowheight = gameheight
    fps = fps_limit
    
    #initialize pygame
    pygame.init()
    #initialize the game window
    displaysurf = pygame.display.set_mode((windowwidth, windowheight))
    #set the description in the window header
    pygame.display.set_caption('PyHearts')
    #initialize the main font for the game
    basicfont = pygame.font.Font('freesansbold.ttf', font_size)
    largefont = pygame.font.Font('freesansbold.ttf', large_font_size)

    #initialize the main canvas for displaying to the window
    frame = pygame.Surface(displaysurf.get_size())
    frame = frame.convert()
    frame.fill(background_color)
    
    #initialize overlay surface for player's hand
    overlay = pygame.Surface((windowwidth,100))
    overlay = overlay.convert()
    overlay.fill(background_color)
