import pytest

from alien_detector.radar import Radar, Position

def test_occurrence_position_is_found():
	radar_map = """\
	ooooooooooooooooooooooooooooo
	o---------------------------o
	o-----------MYSTERIOUS------o
	o---------------------------o
	ooooooooooooooooooooooooooooo
	""".splitlines()
	
	occurrences = list(Radar(radar_map).find_occurrences("MYSTERIOUS"))

	assert str(occurrences) == str([Position(2, 13)]) # dirty str() hack to avoid having to override __eq__


def test_no_occurrences_found():
	radar_map = """\
	ooooooooooooooooooooooooooooo
	o---------------------------o
	o-----------MYSTERIOUS------o
	o---------------------------o
	ooooooooooooooooooooooooooooo
	""".splitlines()
	
	occurrences = list(Radar(radar_map).find_occurrences("NOT_PRESENT_IN_RADAR_MAP"))

	assert occurrences == []


def test_multiple_occurrences_found():
	radar_map = """\
	ooooooooooooooooooooooooooooo
	o--------------X------------o
	o------X--------------------o
	o----------------X----------o
	ooooooooooooooooooooooooooooo
	""".splitlines()
	
	occurrences = list(Radar(radar_map).find_occurrences("X"))

	# dirty str() hack to avoid having to override __eq__
	assert str(occurrences) == str([Position(1, 16), Position(2, 8), Position(3, 18)])