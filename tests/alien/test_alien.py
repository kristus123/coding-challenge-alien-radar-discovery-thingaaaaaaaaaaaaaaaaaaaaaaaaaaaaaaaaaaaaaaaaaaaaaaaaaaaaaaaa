from alien_detector.alien import Alien
from alien_detector.radar import Position


def test_head():
	a = Alien("Billy the alien", "very dangerous",
		"""\
		___
		o-o
		< >
		v|v
		""")

	assert a.head == "___"


def test_str_value():
	a = Alien("Billy the alien", "very dangerous",
		"""\
		___
		o-o
		v-v
		""")

	assert str(a) == "Billy the alien (very dangerous)"


def test_positive_equal_condition():
	assert Alien("Billy", "A", ":^D") == Alien("Mandy", "B", ":^D")


def test_negative_equal_condition():
	assert Alien("Billy", "A", ">:(") != Alien("Mandy", "B", ":^D")