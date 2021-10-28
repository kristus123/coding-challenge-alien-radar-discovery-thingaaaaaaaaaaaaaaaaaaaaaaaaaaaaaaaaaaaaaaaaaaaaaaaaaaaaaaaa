from alien_detector.radar import Position


def test_equal_condition():
	assert Position(1, 2, 3, 4) == Position(1, 2, 3, 4)


def test_equal_condition():
	assert Position(0, 0, 0, 0) != Position(1, 2, 3, 4)