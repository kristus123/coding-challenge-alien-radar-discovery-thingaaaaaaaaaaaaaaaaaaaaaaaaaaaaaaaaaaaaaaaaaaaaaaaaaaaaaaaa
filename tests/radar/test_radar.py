from alien_detector.radar import Radar


def test_specific_area_is_fetched_properly():
	radar_map = """\
	oooooo
	o----o
	o----o
	o----o
	oooooo
	"""
	
	area = Radar(radar_map).get_specific_area(
		line_start=1, 
		char_start=2, 
		char_end=6, 
		line_tail=3)

	assert area == ["----", "----", "----"]