from alien_detector.alien import Alien
from alien_detector.radar import Position


def test_equal_condition():
	assert Position(1, 2, 3, 4) == Position(1, 2, 3, 4)


def test_equal_condition():
	assert Position(0, 0, 0, 0) != Position(1, 2, 3, 4)


def test_position_area_equal_to_size_of_body():

	position = Position(1, 5).relative_to(["___", "o-o", "v-v"])

	assert position == Position(1, 5, 8, 3)