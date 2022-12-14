from __future__ import annotations

import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def solution(s: str) -> int:

    # for n in range(4, len(s), 4):
    #     substr = s[n-4:n]
    #     breakpoint()
    #     found = True
    #     for i, char in enumerate(substr):
    #         if substr.count(char) > 1:
    #             found = False
    #             break

    #     if found:
    #         breakpoint()
    #         return n

    for n in range(0, len(s)-4):
        substr = s[n:n+4]

        found = True

        for char in substr:
            if substr.count(char) > 1:
                found = False
                break

        if found:
            return n+4

    return -1


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        ('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 7),
        ('bvwbjplbgvbhsrlpgdmjqwftvncz', 5),
        ('nppdvjthqldpwncqszvftbrmjlhg', 6),
        ('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', 10),
        ('zcfzfwzzqfrljwzlrfnpqdbhtmscgvj', 11),
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
