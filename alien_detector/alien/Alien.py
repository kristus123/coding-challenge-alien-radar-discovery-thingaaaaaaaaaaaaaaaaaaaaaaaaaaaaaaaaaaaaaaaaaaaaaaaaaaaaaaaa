import textwrap

from radar import Position

class Alien:
	def __init__(self, name, danger_level, body: [str]):
		self._name = name
		self._danger_level = danger_level 
		self._body = textwrap.dedent(body).splitlines()


	@property
	def head(self):
		return self._body[0]


	def position_relative_to(self, p: Position) -> Position:
		return Position(
			p._line, 
			p._char_start,
			p._char_start + len(self._body[0]),
			len(self._body))


	def __eq__(self, other) -> bool:
		return self._body == other


	def __repr__(self):
		return f"{self._name} ({self._danger_level})"