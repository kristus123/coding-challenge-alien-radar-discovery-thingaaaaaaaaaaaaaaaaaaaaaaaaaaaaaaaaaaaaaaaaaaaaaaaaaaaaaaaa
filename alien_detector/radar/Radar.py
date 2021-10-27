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
			return None # The potential alien is not completely visible on the radar.