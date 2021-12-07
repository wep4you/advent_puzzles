# test_day06.py

import pathlib
import pytest
import day06 as day

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day06()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [3,4,3,1,2]

def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example, 18) == 26

def test_part1_example2(example):
    """Test part 1 on example input"""
    assert riddle.part1(example, 80) == 5934

def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example, 256) == 26984457539