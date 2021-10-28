I have been working on a windows environment. I prefer linux, so i set up the project so that it simply works for me.
I chose to keep life simple.

# setup
```shell
# use venv if you want to
pip install -r requirements.txt
```

# Run tests
```shell
python -m pytest
```

# Run program
Put your map in `alien_detector/radar_map.txt`

```shell
# There's probably a better way to structure the program so you don't have to cd into a subdirectory, but i kept life simple
cd alien_detector

python main.py
```