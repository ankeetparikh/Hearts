import pygame, sys, random
from pygame.locals import *

windowwidth = 640
windowheight = 480
fps = 60

WHITE = (250,250,250)
DARK_GREEN = (0,150,0)
BLACK = (0,0,0)
RED = (250,0,0)

background_color = DARK_GREEN
text_color = WHITE
font_size = 10

controls = [K_ESCAPE,K_RETURN]

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
	

def get_Card_Face(num,background):
	global card_dict
	suit = num/13
	number = card_dict[num%13]
	card = pygame.Surface((40,60))
	card.fill(background)
	if suit == 0:
		card_color = BLACK
		suit_img = pygame.image.load('club.bmp')
	elif suit == 1:
		card_color = RED
		suit_img = pygame.image.load('diamond.bmp')
	elif suit == 2:
		card_color = BLACK
		suit_img = pygame.image.load('spade.bmp')
	elif suit == 3:
		card_color = RED
		suit_img = pygame.image.load('heart.bmp')
	numberlabel = basicfont.render(number, True, card_color, WHITE)
	card.blit(numberlabel, (2,2))
	card.blit(numberlabel, (36-5*len(number),48))
	card.blit(suit_img,(10,20))
	return card
	
def wait():
    while True:
        fpsclock.tick(fps)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key in controls:
                return event.key

def initialize():
    global fpsclock,displaysurf,basicfont,background
    
    pygame.init()
    fpsclock = pygame.time.Clock()
    displaysurf = pygame.display.set_mode((windowwidth, windowheight))
    pygame.display.set_caption('PyHearts')
    basicfont = pygame.font.Font('freesansbold.ttf', font_size)

    background = pygame.Surface(displaysurf.get_size())
    background = background.convert()

initialize()
j = 13
hand = random.sample(range(0,52),13)

while True:
	background.fill(background_color)
	displaysurf.blit(background, (0,0))
	
	for i in range(0,j):
		card = get_Card_Face(hand[i],WHITE)
		displaysurf.blit(card,((windowwidth-45*j)/2+i*45, 415))
		
	pygame.display.update()
	keypress = wait()
	
	for event in pygame.event.get(QUIT): # get all the QUIT events
		break
	
	if keypress == K_ESCAPE:
		break
	
	if keypress == K_RETURN:
		j -= 1
		
	fpsclock.tick(fps)

	

