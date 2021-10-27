def find_all(string: str, pattern: str) -> str:
	positions = []
	starting_position = 0
	while True:
		p = string.find(pattern, starting_position)
		if p != -1:
			if p == starting_position:
				starting_position += 1
			else:
				starting_position = p

			if p not in positions:
				positions.append(p)
		else:
			return positions