# A buggy solution to 2016, Day 1
from pathlib import Path

from icecream import ic
import pytest
from typing import NamedTuple
import parse as p

MY_INPUT = Path("input.txt").read_text().strip()

# --> Puzzle solution


class Instruction(NamedTuple):
    turn: str
    blocks: int

    @classmethod
    def fromstr(cls, ins):
        turn,blocks = p.parse("{:l}{:d}", ins)
        result = cls(turn, blocks)
        return result


MOVES = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1),
}

RIGHT_TURNS = {
    "^": ">",
    "v": "<",
    "<": "^",
    ">": "v",
}

LEFT_TURNS = {
    "^": "<",
    "v": ">",
    "<": "v",
    ">": "^",
}


class Cursor(NamedTuple):
    location: tuple[int, int]
    facing: str

    def move(self, instruction):
        if instruction.turn == "L":
            new_direction = LEFT_TURNS[self.facing]
        else:
            new_direction = RIGHT_TURNS[self.facing]

        new_location = (
            self.location[0] + MOVES[new_direction][1],
            self.location[1] + MOVES[new_direction][1],
        )
        return Cursor(new_location, new_direction)


def solve(input_data):
    steps = [Instruction.fromstr(k) for k in input_data.strip().split(",")]
    cursor = Cursor((0, 0), "^")
    for step in steps:
        cursor = cursor.move(step)
    return sum(cursor.location)


# --> Tests


TESTS = [
    ("R2, L3", 5),
]


@pytest.mark.parametrize("test_input,result", TESTS)
def test_example(test_input, result):
    assert solve(test_input) == result


# --> Driver


def main():
    #  Run the test examples with icecream debug-trace turned on
    ic.enable()
    ex = pytest.main(
        [
            __file__,
            "--capture=tee-sys",
            "-v",
        ]
    )
    if ex not in {pytest.ExitCode.OK, pytest.ExitCode.NO_TESTS_COLLECTED}:
        print(f"tests FAILED ({ex})")
        return
    else:
        print("tests PASSED")

    ic.disable()
    print(solve(MY_INPUT))


if __name__ == "__main__":
    main()
