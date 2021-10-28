from alien_detector.alien import AlienCatalog


def test_size_of_catalog():
	assert len(AlienCatalog().aliens) == 2