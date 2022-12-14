from __future__ import annotations

import argparse
import os.path
from collections import defaultdict
from typing import NamedTuple

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


class Move(NamedTuple):
    amount: int
    from_: int
    to: int


def solution(s: str) -> str:

    lines = s.splitlines()
    temp_stacks = defaultdict(list)

    moves: list[Move] = []

    instructions = False
    for line in lines:
        if len(line) == 0:
            instructions = True
            continue
        if instructions:
            inst = [int(s) for s in line.split() if s.isdigit()]
            moves.append(Move(amount=inst[0], from_=inst[1], to=inst[2]))
        else:
            for i, char in enumerate(line):
                if not char.isspace() and char not in '[]':
                    temp_stacks[i].append(char)

    stacks = {}

    for stack in temp_stacks:
        stacks[
            int(temp_stacks[stack][-1])
        ] = list(reversed(temp_stacks[stack][:-1]))

    for move in moves:
        for n in range(move.amount, 0, -1):
            val = stacks[move.from_].pop(len(stacks[move.from_])-n)
            stacks[move.to].append(val)
        # vals = stacks[move.from_][len(stacks[move.from_])-move.amount:]
        # breakpoint()

    final = []
    for key in stacks:
        final.append((key, stacks[key][-1]))

    final_sorted = sorted(final, key=lambda x: x[0])

    # breakpoint()
    return ''.join([x[1] for x in final_sorted])


INPUT_S = '''\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, 'MCD'),
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
