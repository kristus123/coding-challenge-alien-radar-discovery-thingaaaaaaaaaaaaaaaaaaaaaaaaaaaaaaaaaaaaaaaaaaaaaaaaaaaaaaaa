from radar import Position
from .Alien import Alien


class AlienDetector:
	def __init__(self, radar):
		self.radar = radar

	# Another solution could be to fetch a list of areas with a certain length and width
	# and then compare those chunks with the alien body to see if there is a match.
	# That would maybe be a more optimized way of solving this task, and maybe even more readable.
	# If done that way, it would maybe look like this:
	"""
	def find_all(self, alien: Alien) -> (Position):
		for area, position in self.radar.split_map_into_smaller_chunks(alien.height, alien.width):
			if area == alien.body:
				yield position
	"""

	def find_all(self, alien: Alien) -> (Position):
		for p in [p.relative_to(alien.body) for p in self.radar.find_occurrences(alien.head)]:
			if self.radar.area(p) == alien.body:
				yield p