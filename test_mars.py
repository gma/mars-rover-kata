import mars


class TestLocation:
    def test_adding_locations_adds_x_and_y(self) -> None:
        start = mars.Location(x=0, y=0)
        east = mars.Location(x=1, y=0)
        south = mars.Location(x=0, y=-1)

        assert start + east == mars.Location(x=1, y=0)
        assert east + south == mars.Location(x=1, y=-1)

    def test_subtracting_locations_changes_x_and_y(self) -> None:
        start = mars.Location(x=0, y=0)
        east = mars.Location(x=1, y=0)
        south = mars.Location(x=0, y=-1)

        assert start - east == mars.Location(x=-1, y=0)
        assert east - south == mars.Location(x=1, y=1)


class TestRover:
    def test_can_move_forward(self) -> None:
        start = mars.origin
        rover = mars.Rover(location=start, direction=mars.north)

        rover.move('M')

        assert rover.location == start + mars.north

    def test_can_move_forward_then_backtrack(self) -> None:
        start = mars.origin
        rover = mars.Rover(location=start, direction=mars.north)

        rover.move('M')
        rover.backtrack()

        assert rover.location == start

    def test_can_turn_left(self) -> None:
        rover = mars.Rover(location=mars.origin, direction=mars.north)

        rover.move('L')
        rover.move('L')

        assert rover.direction == mars.south

    def test_can_turn_right(self) -> None:
        rover = mars.Rover(location=mars.origin, direction=mars.north)

        rover.move('R')
        rover.move('R')

        assert rover.direction == mars.south

    def test_can_wrap_around_compass_list_to_left(self) -> None:
        rover = mars.Rover(location=mars.origin, direction=mars.north)

        rover.move('L')
        rover.move('L')
        rover.move('L')
        rover.move('L')

        assert rover.direction == mars.north

    def test_can_wrap_around_compass_list_to_right(self) -> None:
        rover = mars.Rover(location=mars.origin, direction=mars.north)

        rover.move('R')
        rover.move('R')
        rover.move('R')
        rover.move('R')

        assert rover.direction == mars.north

    def test_can_turn_left_then_backtrack(self) -> None:
        rover = mars.Rover(location=mars.origin, direction=mars.north)

        rover.move('L')
        rover.backtrack()

        assert rover.direction == mars.north

    def test_can_turn_right_then_backtrack(self) -> None:
        rover = mars.Rover(location=mars.origin, direction=mars.north)

        rover.move('R')
        rover.backtrack()

        assert rover.direction == mars.north

    def test_can_backtrack_multiple_commands(self) -> None:
        rover = mars.Rover(location=mars.origin, direction=mars.north)

        rover.move('M')
        rover.move('R')
        rover.move('M')
        rover.move('L')
        rover.backtrack()
        rover.backtrack()
        rover.backtrack()
        rover.backtrack()

        assert rover.location == mars.origin
        assert rover.direction == mars.north
