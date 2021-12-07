# test_day07.py

import pathlib
import pytest
import day07 as day

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day07()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [16,1,2,0,4,2,7,1,2,14]

pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example) == 37

def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example) == 168