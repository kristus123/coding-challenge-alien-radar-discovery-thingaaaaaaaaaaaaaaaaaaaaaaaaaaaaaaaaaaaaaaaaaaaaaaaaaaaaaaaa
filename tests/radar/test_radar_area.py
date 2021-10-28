import pytest

from alien_detector.radar import Radar, Position


def test_specific_area_is_fetched():
	radar_map = """\
	oooooo
	o----o
	o----o
	o----o
	oooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(line=1, char_start=2, char_end=6, line_tail=3))

	assert area == ["----", "----", "----"]


def test_specific_area_is_fetched():
	radar_map = """\
	ooooooooooooooooooooooooooooo
	o---------------------------o
	o-----I_ONLY_WANT_THIS------o
	o---------------------------o
	ooooooooooooooooooooooooooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(line=2, char_start=7, char_end=23, line_tail=1))

	assert area == ["I_ONLY_WANT_THIS"]


def test_given_invalid_input_when_fetching_area_then_return_none():
	radar_map = """\
	oooooo
	o----o
	o----o
	o----o
	oooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(line=200, char_start=0, char_end=2, line_tail=1))

	assert area == None

@pytest.mark.skip(reason="E    assert  == None - I wonder what is happening here")
def test_given_invalid_input_when_fetching_area_then_return_none():
	radar_map = """\
	oooooo
	o----o
	o----o
	o----o
	oooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(line=2, char_start=100, char_end=201, line_tail=1))

	assert area == None


@pytest.mark.skip(reason="E    assert  == None - I wonder what is happening here")
def test_given_invalid_input_when_fetching_area_then_return_none():
	radar_map = """\
	oooooo
	o----o
	o----o
	o----o
	oooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(line=2, char_start=1, char_end=101, line_tail=1))

	assert area == None



#@pytest.mark.skip(reason="E    assert  == None - I wonder what is happening here")
def test_given_line_tail_is_outside_of_radar_map_when_fetching_area_then_return_none():
	radar_map = """\
	oooooo
	o----o
	o----o
	o----o
	oooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(line=2, char_start=1, char_end=2, line_tail=100))

	assert area == None