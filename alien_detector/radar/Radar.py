from .string_util import find_all
from .Position import Position
from .Area import Area

class Radar:
	def __init__(self, radar_map: [str]):
		self._radar_map = radar_map


	def find_occurrences(self, pattern) -> Position:
		for line in range(len(self._radar_map)):
			for char_position in find_all(self._radar_map[line], pattern):
				yield Position(line, char_position)


	def area(self, p: Position) -> Area:
		try:
			area = []
			for y in p.all_y_positions():
				area.append(self._radar_map[y][p.x1:p.x2])
			return Area(area)
		except IndexError:
			return None # position is outside of radar map

			# I would probably use something else than null because returning a null enforces null-checks
			# and pollutes the inner logic with null-checking

			# There are better and more descriptive ways of dealing with empty values rather than passing null in my opinion
			# But returning a null here was easy and it kept me from over-engineering