import dataclasses
import typing


@dataclasses.dataclass
class Location:
    x: int
    y: int

    def __add__(self, other: 'Location') -> 'Location':
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Location') -> 'Location':
        return self.__class__(self.x - other.x, self.y - other.y)


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

    def undo(self) -> None:
        ...


class MoveForward(Command):
    def execute(self) -> None:
        self.rover.location += self.rover.facing

    def undo(self) -> None:
        self.rover.location -= self.rover.facing


class Turn(Command):
    def index_to_left(self, current_index: int) -> int:
        return current_index - 1

    def index_to_right(self, current_index: int) -> int:
        return current_index + 1

    def turn(self, turn_index: typing.Callable[[int], int]) -> None:
        current_index = compass_points.index(self.rover.facing)
        try:
            self.rover.facing = compass_points[turn_index(current_index)]
        except IndexError:
            self.rover.facing = compass_points[0]


class TurnLeft(Turn):
    def execute(self) -> None:
        self.turn(self.index_to_left)

    def undo(self) -> None:
        self.turn(self.index_to_right)


class TurnRight(Turn):
    def execute(self) -> None:
        self.turn(self.index_to_right)

    def undo(self) -> None:
        self.turn(self.index_to_left)


class Rover:
    commands = {'M': MoveForward, 'L': TurnLeft, 'R': TurnRight}

    def __init__(self, location: Location, facing: Direction) -> None:
        self.location = location
        self.facing = facing
        self.moves: typing.List[Command] = []

    def move(self, instruction: str) -> None:
        command = self.commands[instruction](self)
        command.execute()
        self.moves.append(command)

    def backtrack(self) -> None:
        command = self.moves.pop()
        command.undo()
