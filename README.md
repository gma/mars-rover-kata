Mars Rover Kata
===============

I put this together during the Software Crafters meetup in Manchester, on 30 November 2023.

The focus of the evening was to apply the [Command Pattern] to the [Mars Rover kata].

[Command Pattern]: https://wiki.c2.com/?CommandPattern
[Mars Rover kata]: https://www.codurance.com/katas/mars-rover

The solution
------------

Using the Command pattern suggests that we'll have separate commands for:

- moving forwards
- turning left
- turning right

Each of those commands should be able to access some shared state (i.e. the rover's location),
and should have the same public API/interface. In other words, they all need an `execute()`
method.

I decided to store the rover's current location in a `Location` object that had `x` and `y`
attributes. I realised that in order to move the rover forward, I would only need to modify
`x` or `y`, and that the trick was going to be working out how to change them based on
which way the rover was facing.

What if the direction it was facing was also represented by an object with `x` and `y`
attributes? North would be `x=0, y=1`, east would be `x=1, y=0`, etc. We could then move
forwards by just adding the direction we were currently facing to the current location.

I think that should be enough background for you to explore the code.

Tests are in [test_mars.py](./test_mars.py). The implementation of the commands is in
[mars.py](./mars.py).

Running the tests
-----------------

To run the tests you'll first need to install a couple of things.

Create and activate a virtual environment, into which you can install the dependencies:

    python3 -m venv .venv
    source .venv/bin/activate

Install the dependencies with pip-tools:

    pip install pip-tools
    pip-sync dev-requirements.txt

Run the tests:

    ./test
