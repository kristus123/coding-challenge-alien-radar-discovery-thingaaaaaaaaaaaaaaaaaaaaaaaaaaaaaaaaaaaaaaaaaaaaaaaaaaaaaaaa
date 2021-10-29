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
			for i in range(p._line_tail):
				area.append(self._radar_map[p._line + i][p._char_start:p._char_end])
			return Area(area)
		except IndexError:
			# position is outside of radar map
			return None
			# I would probably use something else than null because returning a null enforces null-checks
			# and there are better ways of dealing with empty values rather than passing null in my opinion
			# But returning a null here was easy and it kept me from over-engineering