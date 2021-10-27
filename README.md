"""
This class works as the adapter between the Radar
and how it knows which area the alien might be at.

It is a little shady that there are two uninitialized instance variables.
That is something that would absolutely become a slippery slope in the future.

In a statically typed language i would solve it by modelling the domain
to the best of my knowledge.

`UnfinishedPosition`* could be turned into a `Position` when `alien_area(...)` is called.
That would make it impossible for an `UnfinishedPosition` object to be passed into
`radar.extract_area(p: Position)`.


	* `UnfinishedPosition` is obviously not the best name,
	but it is the best name i could think of for an
	inexperienced Radar and military rookie like myself.



__  text below turned irrelevant when i created the `Alien` class  ___
__  You can compare my original thought with the current solution  ___

Also the fact that `Position` knows about aliens is
a breach of encapsulation, but that i can live with for now.
I could make an `AlienPosition` class which decoupled
the Position object from knowing about the alien,
but i don't feel this is currently a big issue that will keep me up at night.

(also, if there came a time where it would be
super nice to do this change, it would be easy to accomplish.)

Having an `AlienPosition` would also raise the question to where it makes sense
that this class exists. In the `/alien` module ?

Since the goal of `AlienPosition` is to have radar not be aware that aliens exists
it would not make sense to put it in `/radar`, so then i guess i would have put it in `/alien`.
"""
