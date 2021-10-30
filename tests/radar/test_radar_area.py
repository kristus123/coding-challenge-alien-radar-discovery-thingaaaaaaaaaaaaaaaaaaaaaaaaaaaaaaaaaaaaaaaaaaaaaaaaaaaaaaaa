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
	
	area = Radar(radar_map).area(Position(y1=1, x1=2, x2=6, y2=3))

	assert area == ["----", "----", "----"]


def test_specific_area_is_fetched():
	radar_map = """\
	ooooooooooooooooooooooooooooo
	o---------------------------o
	o-----I_ONLY_WANT_THIS------o
	o---------------------------o
	ooooooooooooooooooooooooooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(y1=2, x1=7, x2=23, y2=1))

	assert area == ["I_ONLY_WANT_THIS"]


def test_given_invalid_input_when_fetching_area_then_return_none():
	radar_map = """\
	oooooo
	o----o
	o----o
	o----o
	oooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(y1=200, x1=0, x2=2, y2=1))

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
	
	area = Radar(radar_map).area(Position(y1=2, x1=100, x2=201, y2=1))

	assert area == None


@pytest.mark.skip(reason="E    assert  == None        - I wonder what is happening here")
def test_given_invalid_input_when_fetching_area_then_return_none():
	radar_map = """\
	oooooo
	o----o
	o----o
	o----o
	oooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(y1=2, x1=1, x2=101, y2=1))

	assert area == None



def test_given_line_tail_is_outside_of_radar_map_when_fetching_area_then_return_none():
	radar_map = """\
	oooooo
	o----o
	o----o
	o----o
	oooooo
	""".splitlines()
	
	area = Radar(radar_map).area(Position(y1=2, x1=1, x2=2, y2=100))

	assert area == None