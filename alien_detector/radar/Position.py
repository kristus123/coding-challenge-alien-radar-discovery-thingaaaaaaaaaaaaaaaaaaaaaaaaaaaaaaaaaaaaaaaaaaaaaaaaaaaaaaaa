"""
It is a little shady that there are two uninitialized instance variables.
That is something that would absolutely become a slippery slope in the future.

In a statically typed language i would solve it by modelling the domain
to the best of my knowledge.

One class could be named `Position2` while another was named `Position4` or something along those lines
I could do a similar solution here, but then i would need to change code
and right now I REALLLLLLYYYY feel the downsides of using a text editor vs an IDE so i will just let it be for now.

"""

class Position:
	# I would make the parameters line up with the order the values are displayed in __repr__ that would make life much easier
	# But for now i will just live with it
	def __init__(self, line, char_start, char_end=None, line_tail=None):
		self._line = line
		self._char_start = char_start
		
		self._char_end = char_end
		self._line_tail = line_tail

		# Also i would not have the instance variables be 'private' (_char_end) (but keeping it as is for above mentioned lazy reasons)
		
		# Also i would rename them to x1, x2, y1, y2 to keep things consistent.
		# There are two reasons why
		# 1. the current names expose the implementation of the Radar.py, which uses character positions and text
		# 		- using x1, y1 etc would encapsulate this
		# 2. Keeping things consistent is a powerful tool


	@property
	def x1(self):
		return self._char_start


	@property
	def x2(self):
		return self._char_end


	def all_y_positions(self) -> (int):
		for i in range(self._line_tail):
			yield self._line + i


	"""
	body: [str] could be its own class to avoid having to rely on 'primitive data types'
	But i ain't getting paid to do sexy domain modelling tonight so i will leave it be.
	"""
	def relative_to(self, body: [str]):
		return Position(
			self._line, 
			self._char_start, 
			self._char_start + len(body[0]),
			len(body))



	def __repr__(self):
		return f"position(X1={self._char_start}, X2={self._char_end} : Y1={self._line}, Y2={self._line_tail})"

	# hack : https://stackoverflow.com/questions/46708659/isinstance-fails-for-a-type-imported-via-package-and-from-the-same-module-direct
	# Probably because i have not followed best pracises when it comes to structuring python and pytest projects
	def __eq__(s, o):
		return str(s) == str(o)