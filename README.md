# Alien detection software
I have been working in a windows environment (I prefer linux).
It will probably work fine in other environments as well (though i have not tested).

## A word on defensive programming
There is not much validation to check if x > y or whether values are as expected when passed around.
The pragmatic solution has been to not focus on this.

if i were to take external input into my domain/project i would think otherwise. 
an Anti-Corruption layer is a pretty cool concept for this.


## setup
```shell
# use venv if you want to
pip install -r requirements.txt
```

## Run tests
```shell
python -m pytest
```

## Run program
Put your map in `alien_detector/radar_map.txt`

```shell
# There's probably a better way to structure the program so you don't have to cd into a subdirectory, but i kept life simple

cd alien_detector

python main.py
```

disclaimer:
i have not bothered with doing proper `git committing`. I did not see any value in proving that i am able to use git in a way that makes the changes and history readable (which also makes life easy for me+others when we come to a point where we need to dig into the history).