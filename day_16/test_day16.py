# test_day16.py

import pathlib
import pytest
import day16 as day

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day16()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)

@pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == ...

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example) == ...