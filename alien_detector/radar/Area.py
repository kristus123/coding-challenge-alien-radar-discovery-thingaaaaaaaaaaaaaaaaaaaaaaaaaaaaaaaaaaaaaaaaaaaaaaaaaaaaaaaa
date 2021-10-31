import textwrap


class Area:
	def __init__(self, body: [str]):
		self._body = body
			

	@property
	def head(self):
		return self._body[0]


	@property
	def length(self):
		return len(self._body)


	def __eq__(self, other) -> bool:
		return self._body == other


	def __repr__(self):
		return "\n".join([i for i in self._body[1:]])