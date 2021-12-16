# test_day15.py

import pathlib
import pytest
import day15 as day
import numpy as np

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day15()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example(example):
    """Test that input is parsed properly"""
    assert (example == np.array([
        [1,1,6,3,7,5,1,7,4,2],
        [1,3,8,1,3,7,3,6,7,2],
        [2,1,3,6,5,1,1,3,2,8],
        [3,6,9,4,9,3,1,5,6,9],
        [7,4,6,3,4,1,7,1,1,1],
        [1,3,1,9,1,2,8,1,3,7],
        [1,3,5,9,9,1,2,4,2,1],
        [3,1,2,5,4,2,1,6,3,9],
        [1,2,9,3,1,3,8,5,2,1],
        [2,3,1,1,9,4,4,5,8,1]
    ])).all()

def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example) == 40

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example) == ...