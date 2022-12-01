from __future__ import annotations

import argparse
import os.path
from collections import defaultdict

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solution(s: str) -> int:

    lines = s.splitlines()

    i = 0
    elves_to_calories: dict[int, int] = defaultdict(int)

    for line in lines:
        if len(line) == 0:
            i += 1
        else:
            elves_to_calories[i] += int(line)

    cur_max = max(elves_to_calories.values())
    # cur_max = 0
    # cur_key = 0
    # for k, v in elves_to_calories.items():
    #     if v >= cur_max:
    #         cur_max = v
    #         cur_key = k

    return cur_max


INPUT_S = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 24000),
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
