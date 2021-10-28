"""
It is a little shady that there are two uninitialized instance variables.
That is something that would absolutely become a slippery slope in the future.

In a statically typed language i would solve it by modelling the domain
to the best of my knowledge.

`UnfinishedPosition`* could be turned into a `Position` when `alien_area(...)` is called.
That would make it impossible for an `UnfinishedPosition` object to be passed into
`radar.extract_area(p: Position)`.


* `UnfinishedPosition` is obviously not the best name
"""

class Position:
	# I would make the parameters line up with the order the values are displayed in __repr__ that would make life much easier
	# But for now i will just live with it
	def __init__(self, line, char_start, char_end=None, line_tail=None):
		self._line = line
		self._char_start = char_start
		
		self._char_end = char_end
		self._line_tail = line_tail


	def __repr__(self):
		return f"position(X1={self._char_start}, X2={self._char_end} : Y1={self._line}, Y2={self._line_tail})"

	# hack : https://stackoverflow.com/questions/46708659/isinstance-fails-for-a-type-imported-via-package-and-from-the-same-module-direct
	# Probably because i have (probably) not followed best pracises when it comes to structuring python projects
	def __eq__(s, o):
		return str(s) == str(o)