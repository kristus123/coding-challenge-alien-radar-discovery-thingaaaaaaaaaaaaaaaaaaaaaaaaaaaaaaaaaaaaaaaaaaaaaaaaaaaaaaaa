from alien_detector.alien import AlienDetector, Alien
from alien_detector.radar import Area, Position, Radar

alien = Alien("Billy", "scary",
	"""\
	___
	:^D
	___
	""")

radar = Radar([
	"----------------",
	"----------------",
	"----------___---",
	"----------:^D---",
	"----------___---",
	"----------------",

])

alienDetector = AlienDetector(radar)

expected_position = Position(2, 10, 13, 3)


def test_position_of_alien_is_correct():
	alien_positions = alienDetector.find_all(alien)

	assert list(alien_positions) == [expected_position]

	assert radar.area(expected_position) == ["___", ":^D", "___"] 


def test_no_aliens_found():
	a = Alien("alien from another galaxy", "Never observed in our galaxy", "<*_*>")

	alien_positions = alienDetector.find_all(a)

	assert list(alien_positions) == []