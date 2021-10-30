from alien_detector.alien import Alien
from alien_detector.radar import Position


def test_equal_condition():
	assert Position(1, 2, 3, 4) == Position(1, 2, 3, 4)


def test_equal_condition():
	assert Position(0, 0, 0, 0) != Position(1, 2, 3, 4)


def test_position_area_equal_to_size_of_body():

	position = Position(1, 5).relative_to(["___", "o-o", "v-v"])

	assert position == Position(1, 5, 8, 3)


def test_all_y_positions():

	position = Position(10, 5, 2, 5)

	assert list(position.all_y_positions()) == [10, 11, 12, 13, 14]


def test_given_y2_is_zero_when_getting_all_y_positions_then_return_empty_list():

	position = Position(10, 5, 2, 0)

	assert list(position.all_y_positions()) == []

	# Not 100% sure whether this is the best default behavior