import randompy
class Deck(object):
	def shuffle(self):
		suits = ["spades", "hearts", "clubs", "diamonds"]
		ranks = ["1", "2", "3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
		self.cards = []
		for suit in suits:
			for rank in ranks:
				cards.append(rank + "of" + suit)
		random.shuffle(self.cards)
	def deal(self):
		return self.cards.pop()
d = Deck()
d.shuffle()
print(d.deal())
print(d.deal())
print(d.deal())
