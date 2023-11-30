import dataclasses


@dataclasses.dataclass
class Location:
    x: int
    y: int

    def __add__(self, other: 'Location') -> 'Location':
        return self.__class__(self.x + other.x, self.y + other.y)


Direction = Location


origin = Location(0, 0)

north = Direction(0, 1)
south = Direction(0, -1)
east = Direction(1, 0)
west = Direction(-1, 0)

compass_points = [north, east, south, west]


class Command:
    def __init__(self, rover: 'Rover') -> None:
        self.rover = rover

    def execute(self) -> None:
        ...


class MoveForward(Command):
    def execute(self) -> None:
        self.rover.location += self.rover.facing


class TurnLeft(Command):
    def execute(self) -> None:
        facing_index = compass_points.index(self.rover.facing)
        self.rover.facing = compass_points[facing_index - 1]


class TurnRight(Command):
    def execute(self) -> None:
        facing_index = compass_points.index(self.rover.facing)
        try:
            self.rover.facing = compass_points[facing_index + 1]
        except IndexError:
            self.rover.facing = compass_points[0]


class Rover:
    commands = {'M': MoveForward, 'L': TurnLeft, 'R': TurnRight}

    def __init__(self, location: Location, facing: Direction) -> None:
        self.location = location
        self.facing = facing

    def move(self, instruction: str) -> None:
        self.commands[instruction](self).execute()
