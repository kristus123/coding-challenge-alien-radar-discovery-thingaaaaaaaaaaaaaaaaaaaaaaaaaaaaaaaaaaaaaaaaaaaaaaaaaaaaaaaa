from alien_detector.radar.string_util import find_all

def test_given_one_matching_pattern():
	assert find_all("X_____", "X") == [0]
	assert find_all("_X____", "X") == [1]
	assert find_all("__X___", "X") == [2]
	assert find_all("___X__", "X") == [3]
	assert find_all("____X_", "X") == [4]
	assert find_all("_____X", "X") == [5]


def test_given_two_matching_patterns():
	assert find_all("X___________X", "X") == [0, 12]
	assert find_all("_X_________X_", "X") == [1, 11]
	assert find_all("__X_______X__", "X") == [2, 10]
	assert find_all("___X_____X___", "X") == [3, 9]
	assert find_all("____X___X____", "X") == [4, 8]
	assert find_all("_____X_X_____", "X") == [5, 7]
	assert find_all("______X______", "X") == [6]