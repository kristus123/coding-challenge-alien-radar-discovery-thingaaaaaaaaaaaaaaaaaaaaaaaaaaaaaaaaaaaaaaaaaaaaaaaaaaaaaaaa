import textwrap

from radar import Area

class Alien:
	def __init__(self, name: str, danger_level: str, body: str):
		self._name = name
		self._danger_level = danger_level 
		self.body = Area(textwrap.dedent(body).splitlines())


	# Law of demeter. There is no reason for others to know that Area.py is used in the underlying implementation
	@property
	def head(self):
		return self.body.head
	# 'inheritance increase coupling'
	# Even though i am not doing pure subclassing, i am still coupled to the implementation of Area.py
	# I am probably overthinking it in this scenario, but it is worth having in mind the potential ripple effect this causes.

	def __eq__(self, other) -> bool:
		return self.body == other


	def __repr__(self):
		return f"{self._name} ({self._danger_level})"