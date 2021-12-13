# test_day13.py

import pathlib
import pytest
import numpy as np
import day13 as day

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day13()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)


def test_parse_example(example):
    """Test that input is parsed properly"""
    assert (example[0] == np.array([
        [6, 10],
        [0, 14],
        [9, 10],
        [0, 3],
        [10, 4],
        [4, 11],
        [6, 0],
        [6, 12],
        [4, 1],
        [0, 13],
        [10, 12],
        [3, 4],
        [3, 0],
        [8, 4],
        [1, 10],
        [2, 14],
        [8, 10],
        [9, 0]
    ])).all()
    assert (example[1] == np.array([
        ['y', 7],
        ['x', 5]
    ])).all()

def test_part1_initArray(example):
    """Test initArray on example input"""
    assert (riddle.initArray(example) == np.array([
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
    ])).all()

def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example, 1) == 17

def test_part1_example2(example):
    """Test part 1 on example input"""
    assert riddle.part1(example, 2) == 16

def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example) == (
        '#####\n' +
        '#   #\n' +
        '#   #\n' +
        '#   #\n' +
        '#####\n' +
        '     \n' +
        '     \n')