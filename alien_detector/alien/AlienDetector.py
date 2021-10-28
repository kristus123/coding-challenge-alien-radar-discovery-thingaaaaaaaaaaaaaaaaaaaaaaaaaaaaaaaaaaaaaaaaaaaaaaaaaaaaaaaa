from radar import Position
from .Alien import Alien


class AlienDetector:
	def __init__(self, radar):
		self.radar = radar


	def find_all(self, alien: Alien) -> (Position):
		for alien_position in [alien.position_relative_to(p) for p in self.radar.find_occurrences(alien.head)]:
			if self.radar.area(alien_position) == alien:
				yield alien_position