class Auto:
	def __init__(self):
		pass

	def auto(Player,sofar):
		clubs = []
		diamonds = []
		spades = []
		hearts = []
		for i in range(13):
			if i/13 == 0:
				clubs.append(i)
			if i/13 == 1:
				diamonds.append(i)
			if i/13 == 2:
				spades.append(i)
			if i/13 == 3:
				hearts.append(i)
		
		'''
		If you have two of clubs, you must play it 
		'''
		if Player.hasTwoOfClubs:
			play = 0
			clubs.remove(0)

		''' 
		If you're leading the trick, play the lowest card across any suit
		'''
		if len(sofar)==0:
			all_cards = [clubs,diamonds,spades,hearts]
			indices = []
			lowest = []
			for i in all_cards:
				if len(i)>0:
					lowest.append(i%13)
					indices.append(all_cards.index(i))
			min_index = lowest.index(min(lowest))
			play = all_cards(indices[min_index][0])

					





