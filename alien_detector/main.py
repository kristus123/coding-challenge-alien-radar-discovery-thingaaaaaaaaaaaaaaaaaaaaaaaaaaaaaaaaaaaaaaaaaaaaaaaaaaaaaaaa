from radar import Radar
from alien import AlienCatalog, AlienDetector


with open('radar_map.txt', 'r') as r:
	radar_map = [l.rstrip("\n") for l in r.readlines()]

radar = Radar(radar_map)
alienDetector = AlienDetector(radar)

alienCatalog = AlienCatalog()

for alien in alienCatalog.aliens:
	for position in alienDetector.find(alien):
		if position:
			print(f"Found {alien} at {position}")