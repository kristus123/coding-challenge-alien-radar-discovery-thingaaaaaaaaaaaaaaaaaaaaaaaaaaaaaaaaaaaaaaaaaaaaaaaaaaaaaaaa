from radar import Position
from .Alien import Alien


class AlienDetector:
	def __init__(self, radar):
		self.radar = radar


	def find_all(self, alien: Alien) -> (Position):
		for p in [p.relative_to(alien.body) for p in self.radar.find_occurrences(alien.head)]:
			if self.radar.area(p) == alien.body:
				yield p