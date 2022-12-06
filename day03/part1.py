from __future__ import annotations

import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def get_points(char: str) -> int:

    if char.isupper():
        val = ord(char) - 64 + 26
    else:
        val = ord(char) - 96

    return val


def solution(s: str) -> int:

    sum_ = 0

    for line in s.splitlines():
        comp1 = set(line[:len(line)//2])
        comp2 = set(line[len(line)//2:])

        common_item = comp1 & comp2
        for item in common_item:
            sum_ += get_points(item)

    return sum_


INPUT_S = '''\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 157),
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
