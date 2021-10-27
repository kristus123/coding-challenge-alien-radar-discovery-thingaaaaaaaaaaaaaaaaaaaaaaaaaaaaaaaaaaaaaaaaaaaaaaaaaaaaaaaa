from alien_detector.radar.string_util import find_all

def test_given_one_matching_pattern():
	assert find_all("X_____", "X") == [0]
	assert find_all("_X____", "X") == [1]
	assert find_all("__X___", "X") == [2]
	assert find_all("___X__", "X") == [3]


def test_given_two_matching_patterns():
	assert find_all("X_______X__", "X") == [0, 8]
	assert find_all("_X_____X___", "X") == [1, 7]
	assert find_all("__X___X____", "X") == [2, 6]
	assert find_all("___X_X__  _", "X") == [3, 5]