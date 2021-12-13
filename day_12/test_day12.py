# test_day12.py

import pathlib
import pytest
import day12 as day

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day12()

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return riddle.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return riddle.parse(puzzle_input)

@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {
        'start': [ 'A', 'b'],
        'A': ['start', 'c', 'b', 'end'],
        'b': ['start', 'A', 'd', 'end'],
        'c': ['A'],
        'd': ['b'],
        'end': ['A', 'b']
    }

def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert example2 == {
        'dc': ['end', 'start', 'HN', 'LN', 'kj'],
        'end': ['dc', 'HN'],
        'HN': ['start', 'dc', 'end', 'kj'],
        'start': ['HN', 'kj', 'dc'],
        'kj': ['start', 'sa', 'HN', 'dc'],
        'LN': ['dc'],
        'sa': ['kj']
    }

def test_parse_example3(example3):
    """Test that input is parsed properly"""
    assert example3 == {
        'fs': ['end', 'he', 'DX', 'pj'],
        'end': ['fs', 'zg'],
        'he': ['DX', 'fs', 'pj', 'RW', 'WI', 'zg'],
        'DX': ['he', 'start', 'pj', 'fs'],
        'start': ['DX', 'pj', 'RW'],
        'pj': ['DX', 'zg', 'he', 'RW', 'start', 'fs'],
        'zg': ['end', 'sl', 'pj', 'RW', 'he'],
        'sl': ['zg'],
        'RW': ['he', 'pj', 'zg', 'start'],
        'WI': ['he'],
    }

def test_part1_example1(example1):
    """Test part 1 on example1 input"""
    pathArray = riddle.part1(example1)
    assert pathArray[0] == 10
    assert pathArray[1] == [
        ['start','A','c','A','b','A','end'],
        ['start','A','c','A','b','end'],
        ['start','A','c','A','end'],
        ['start','A','b','A','c','A','end'],
        ['start','A','b','A','end'],
        ['start','A','b','end'],
        ['start','A','end'],
        ['start','b','A','c','A','end'],
        ['start','b','A','end'],
        ['start','b','end']
    ]

def test_part1_example2(example2):
    """Test part 1 on example2 input"""
    pathArray = riddle.part1(example2)
    assert pathArray[0] == 19
    assert pathArray[1] == [
        ['start', 'HN', 'dc', 'end'],
        ['start', 'HN', 'dc', 'HN', 'end'],
        ['start', 'HN', 'dc', 'HN', 'kj', 'HN', 'end'],
        ['start', 'HN', 'dc', 'kj', 'HN', 'end'],
        ['start', 'HN', 'end'],
        ['start', 'HN', 'kj', 'HN', 'dc', 'end'],
        ['start', 'HN', 'kj', 'HN', 'dc', 'HN', 'end'],
        ['start', 'HN', 'kj', 'HN', 'end'],
        ['start', 'HN', 'kj', 'dc', 'end'],
        ['start', 'HN', 'kj', 'dc', 'HN', 'end'],
        ['start', 'kj', 'HN', 'dc', 'end'],
        ['start', 'kj', 'HN', 'dc', 'HN', 'end'],
        ['start', 'kj', 'HN', 'end'],
        ['start', 'kj', 'dc', 'end'],
        ['start', 'kj', 'dc', 'HN', 'end'],
        ['start', 'dc', 'end'],
        ['start', 'dc', 'HN', 'end'],
        ['start', 'dc', 'HN', 'kj', 'HN', 'end'],
        ['start', 'dc', 'kj', 'HN', 'end'],
    ]

def test_part1_example3(example3):
    """Test part 1 on example3 input"""
    pathArray = riddle.part1(example3)
    assert pathArray[0] == 226

def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert riddle.part2(example1) == 36

def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert riddle.part2(example2) == 103

def test_part2_example3(example3):
    """Test part 2 on example input"""
    assert riddle.part2(example3) == 3509