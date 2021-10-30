import textwrap

from radar import Position

class Alien:
	def __init__(self, name: str, danger_level: str, body: [str]):
		self._name = name
		self._danger_level = danger_level 
		self.body = textwrap.dedent(body).splitlines()


	@property
	def head(self):
		return self.body[0]


	def __eq__(self, other) -> bool:
		return self.body == other


	def __repr__(self):
		return f"{self._name} ({self._danger_level})"