from radar import Radar
from alien import AlienCatalog, AlienDetector


with open('radar_map.txt', 'r') as r:
	radar_map = [l.rstrip("\n") for l in r.readlines()]

radar = Radar(radar_map)
alienDetector = AlienDetector(radar)

for alien in AlienCatalog().aliens:
	for position in alienDetector.find_all(alien):
		if position:
			print(f"Found {alien} at {position}")