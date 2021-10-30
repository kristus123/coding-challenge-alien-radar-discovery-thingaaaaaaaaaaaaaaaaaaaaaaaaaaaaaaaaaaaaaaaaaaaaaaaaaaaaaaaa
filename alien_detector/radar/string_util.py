def find_all(string: str, pattern: str) -> [int]:
	positions = []
	starting_position = 0
	while True:
		p = string.find(pattern, starting_position)
		if p == -1:
			return positions

		if p == starting_position: # To avoid an infinite loop in case p == 0
			starting_position += 1
		else:
			starting_position = p

		if p not in positions:
			positions.append(p)
