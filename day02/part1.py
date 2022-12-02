from __future__ import annotations

import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def round_points(x, y):

    # Rock VS sciccors
    if x == 'A' and y == 'Z':
        return 0  # oponent won
    # Rock vs paper
    elif x == 'A' and y == 'Y':
        return 6  # you won
    # Rock vs rock
    elif x == 'A' and y == 'X':
        return 3  # draw
    # Paper VS sciccors
    elif x == 'B' and y == 'Z':
        return 6  # you won
    # Paper vs rock
    elif x == 'B' and y == 'X':
        return 0  # youlost
    # paper vs paper
    elif x == 'B' and y == 'Y':
        return 3  # draw
    elif x == 'C' and y == 'Y':
        return 0  # opponent won
    elif x == 'C' and y == 'X':
        return 6  # you won
    elif x == 'C' and y == 'Z':
        return 3  # draw
    else:
        return 3  # dunno


def solution(s: str) -> int:

    score = 0

    scores = {
        'X': 1,  # rock
        'Y': 2,  # paper
        'Z': 3,  # siccors
    }

    for line in s.splitlines():
        they, me = line.split()
        score += round_points(they, me) + scores[me]

    return score


INPUT_S = '''\
A Y
B X
C Z
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 15),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert solution(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f:
        print(solution(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
