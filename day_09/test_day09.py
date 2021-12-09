# test_day09.py

import pathlib
import pytest
import day09 as day

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day09()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [
        [2,1,9,9,9,4,3,2,1,0],
        [3,9,8,7,8,9,4,9,2,1],
        [9,8,5,6,7,8,9,8,9,2],
        [8,7,6,7,8,9,6,7,8,9],
        [9,8,9,9,9,6,5,6,7,8]
    ]

def test_part1_LowPoint():
    """Test part 1 on example input"""
    assert riddle.isLowPoint(1, [2, 9, 9])
    assert riddle.isLowPoint(0, [1, 1])
    assert riddle.isLowPoint(5, [8, 8, 6, 6])
    assert riddle.isLowPoint(5, [6, 6, 6])

def test_part1_HighPoint():
    """Test part 1 on example input"""
    assert riddle.isLowPoint(4, [9, 9, 3]) == False
    assert riddle.isLowPoint(9, [8, 8]) == False
    assert riddle.isLowPoint(7, [6, 8, 8, 8]) == False
    assert riddle.isLowPoint(9, [8, 6, 9]) == False

def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example) == 15

def test_part2_basin_4(example):
    """Test part 2 on example input"""
    assert riddle.countBasin({'row': 1, 'col': 0}, example) == 3
    assert riddle.countBasin({'row': 9, 'col': 0}, example) == 9
    assert riddle.countBasin({'row': 2, 'col': 2}, example) == 14
    assert riddle.countBasin({'row': 6, 'col': 4}, example) == 9

def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example) == 1134