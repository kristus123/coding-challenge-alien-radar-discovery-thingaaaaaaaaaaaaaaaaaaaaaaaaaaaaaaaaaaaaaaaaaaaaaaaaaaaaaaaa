from radar import Area

"""
It is a little shady that there are two uninitialized instance variables.
That is something that would absolutely become a slippery slope in the future.

It could be solved by modelling the domain and having the 'compiler' enforce these rules.

One class could be named `Position2` while another was named `Position4` or something along those lines
I could do a similar solution here, but then i would need to change code
and right now I REALLLLLLYYYY feel the downsides of using a text editor vs an IDE so i will just let it be for now.
"""

class Position:
	def __init__(self, y1, x1, x2=None, y2=None):
		self.y1 = y1
		self.y2 = y2

		self.x1 = x1
		self.x2 = x2


	def all_y_positions(self) -> (int):
		for i in range(self.y2):
			yield self.y1 + i


	def relative_to(self, area: Area):
		return Position(self.y1, self.x1, self.x1 + len(area.head), area.length)


	def __repr__(self):
		return f"position(Y1={self.y1}, X1={self.x1} : X2={self.x2}, Y2={self.y2})"


	# hack : https://stackoverflow.com/questions/46708659/isinstance-fails-for-a-type-imported-via-package-and-from-the-same-module-direct
	# Probably because i have not followed best pracises when it comes to structuring python and pytest projects
	def __eq__(s, o):
		return str(s) == str(o)