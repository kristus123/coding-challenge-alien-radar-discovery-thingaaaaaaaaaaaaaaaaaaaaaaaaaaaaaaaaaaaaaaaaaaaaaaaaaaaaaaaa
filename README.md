i ran this on windows by doing the following

# setup
````shell
# use venv if you want to
pip install -r requirements.txt
```


# Run tests
````shell
python -m pytest

```


# Run program
Put your map in `alien_detector/radar_map.txt`

```shell
cd alien_detector && python main.py # There's probably a better way so you don't have to cd into a subdirectory, but i kept life simple
```