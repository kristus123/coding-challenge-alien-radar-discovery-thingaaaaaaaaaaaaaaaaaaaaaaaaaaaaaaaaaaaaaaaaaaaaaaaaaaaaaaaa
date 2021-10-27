class Area:
	def __init__(self, body: [str]):
		self._body = body


	def __eq__(self, other) -> bool:
		return self._body == other


	def __repr__(self):
		return "\n".join([i for i in self._body[1:]])