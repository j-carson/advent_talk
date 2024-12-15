from pathlib import Path
import sys

from icecream import ic
import parse as p
import pytest

SAMPLE_INPUT = Path("input-sample.txt").read_text().strip()
SAMPLE_SOLUTION = 0

MY_INPUT = Path("input.txt").read_text().strip()

# --> Puzzle solution


def solve(input_data):
    ic(input_data)
    return 0


# --> Tests


def test_something():
    # Pretend the test failed
    raise Exception("oops")


def test_example():
    assert solve(SAMPLE_INPUT) == SAMPLE_SOLUTION


# --> Driver

if __name__ == "__main__":
    #  Run the test examples with icecream debug-trace turned on
    ic.enable()
    ex = pytest.main([__file__, "--capture=tee-sys", "-v"])
    if ex not in {pytest.ExitCode.OK, pytest.ExitCode.NO_TESTS_COLLECTED}:
        print(f"tests FAILED ({ex})")
        sys.exit(1)
    else:
        print("tests PASSED")

    #  Actual input data generally has more iterations, turn off ic
    ic.disable()
    result = solve(my_input)
    print(result)
