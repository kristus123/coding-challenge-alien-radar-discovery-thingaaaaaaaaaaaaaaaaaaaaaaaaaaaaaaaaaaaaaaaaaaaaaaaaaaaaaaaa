from .Alien import Alien

class AlienCatalog:
	def __init__(self):
		self.aliens = [
			Alien(
				"Sneaky alien",
				"high-level threat",
				"""\
					--o-----o--
					---o---o---
					--ooooooo--
					-oo-ooo-oo-
					ooooooooooo
					o-ooooooo-o
					o-o-----o-o
					---oo-oo---
				"""),
			Alien(
				"Slow alien",
				"low-level threat",
				"""\
					---oo---
					--oooo--
					-oooooo-
					oo-oo-oo
					oooooooo
					--o--o--
					-o-oo-o-
					o-o--o-o
				""")
		]