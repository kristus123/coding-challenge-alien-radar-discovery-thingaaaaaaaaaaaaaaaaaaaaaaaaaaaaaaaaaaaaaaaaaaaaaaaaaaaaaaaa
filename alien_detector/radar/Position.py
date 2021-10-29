"""
It is a little shady that there are two uninitialized instance variables.
That is something that would absolutely become a slippery slope in the future.

In a statically typed language i would solve it by modelling the domain
to the best of my knowledge.

One class could be named `Position2` while another was named `Position4` or something along those lines

"""

class Position:
	# I would make the parameters line up with the order the values are displayed in __repr__ that would make life much easier
	# But for now i will just live with it
	def __init__(self, line, char_start, char_end=None, line_tail=None):
		self._line = line
		self._char_start = char_start
		
		self._char_end = char_end
		self._line_tail = line_tail

		# Also i would not have the instance variables be 'private' (_char_end)
		# and i would rename them to x1, x2, y1, y2 to keep things consistent.
		# There are two reasons why
		# 1. the current names expose the implementation of the Radar, which uses character positions
		# 		- using x1, y1 etc would encapsulate this
		# 2. Keeping things consistent is a powerful tool often overlooked


	def __repr__(self):
		return f"position(X1={self._char_start}, X2={self._char_end} : Y1={self._line}, Y2={self._line_tail})"

	# hack : https://stackoverflow.com/questions/46708659/isinstance-fails-for-a-type-imported-via-package-and-from-the-same-module-direct
	# Probably because i have (probably) not followed best pracises when it comes to structuring python projects
	def __eq__(s, o):
		return str(s) == str(o)