# test_day11.py

import pathlib
import pytest
import day11 as day

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day11()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [
        [5,4,8,3,1,4,3,2,2,3],
        [2,7,4,5,8,5,4,7,1,1],
        [5,2,6,4,5,5,6,1,7,3],
        [6,1,4,1,3,3,6,1,4,6],
        [6,3,5,7,3,8,5,4,7,8],
        [4,1,6,7,5,2,4,6,4,5],
        [2,1,7,6,8,4,1,7,2,1],
        [6,8,8,2,8,8,1,1,3,4],
        [4,8,4,6,8,4,8,5,5,4],
        [5,2,8,3,7,5,1,5,2,6]
    ]

def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert example2 == [
        [1,1,1,1,1],
        [1,9,9,9,1],
        [1,9,1,9,1],
        [1,9,9,9,1],
        [1,1,1,1,1]
    ]

def test_part1_example2_increaseEnergy(example2):
    """Test part 1 on example2 input - Step 1"""
    step1 = riddle.increaseEnergy(example2)
    assert step1 == [
        [3,4,5,4,3],
        [4,0,0,0,4],
        [5,0,0,0,5],
        [4,0,0,0,4],
        [3,4,5,4,3]
    ]
    """Test part 1 on example2 input - Step 2"""
    step2 = riddle.increaseEnergy(step1)
    assert step2 == [
        [4,5,6,5,4],
        [5,1,1,1,5],
        [6,1,1,1,6],
        [5,1,1,1,5],
        [4,5,6,5,4]
    ]

def test_part1_example_increaseEnergy(example):
    """Test part 1 on example input - Step 1"""
    step1 = riddle.increaseEnergy(example)
    assert step1 == [
        [6,5,9,4,2,5,4,3,3,4],
        [3,8,5,6,9,6,5,8,2,2],
        [6,3,7,5,6,6,7,2,8,4],
        [7,2,5,2,4,4,7,2,5,7],
        [7,4,6,8,4,9,6,5,8,9],
        [5,2,7,8,6,3,5,7,5,6],
        [3,2,8,7,9,5,2,8,3,2],
        [7,9,9,3,9,9,2,2,4,5],
        [5,9,5,7,9,5,9,6,6,5],
        [6,3,9,4,8,6,2,6,3,7]
    ]
    """Test part 1 on example input - Step 2"""
    step2 = riddle.increaseEnergy(step1)
    assert step2 == [
        [8,8,0,7,4,7,6,5,5,5],
        [5,0,8,9,0,8,7,0,5,4],
        [8,5,9,7,8,8,9,6,0,8],
        [8,4,8,5,7,6,9,6,0,0],
        [8,7,0,0,9,0,8,8,0,0],
        [6,6,0,0,0,8,8,9,8,9],
        [6,8,0,0,0,0,5,9,4,3],
        [0,0,0,0,0,0,7,4,5,6],
        [9,0,0,0,0,0,0,8,7,6],
        [8,7,0,0,0,0,6,8,4,8]
    ]
    """Test part 1 on example input - Step 3"""
    step3 = riddle.increaseEnergy(step2)
    assert step3 == [
        [0,0,5,0,9,0,0,8,6,6],
        [8,5,0,0,8,0,0,5,7,5],
        [9,9,0,0,0,0,0,0,3,9],
        [9,7,0,0,0,0,0,0,4,1],
        [9,9,3,5,0,8,0,0,6,3],
        [7,7,1,2,3,0,0,0,0,0],
        [7,9,1,1,2,5,0,0,0,9],
        [2,2,1,1,1,3,0,0,0,0],
        [0,4,2,1,1,2,5,0,0,0],
        [0,0,2,1,1,1,9,0,0,0]
    ]
    """Test part 1 on example input - Step 4"""
    step4 = riddle.increaseEnergy(step3)
    assert step4 == [
        [2,2,6,3,0,3,1,9,7,7],
        [0,9,2,3,0,3,1,6,9,7],
        [0,0,3,2,2,2,1,1,5,0],
        [0,0,4,1,1,1,1,1,6,3],
        [0,0,7,6,1,9,1,1,7,4],
        [0,0,5,3,4,1,1,1,2,2],
        [0,0,4,2,3,6,1,1,2,0],
        [5,5,3,2,2,4,1,1,2,2],
        [1,5,3,2,2,4,7,2,1,1],
        [1,1,3,2,2,3,0,2,1,1]
    ]
    """Test part 1 on example input - Step 5"""
    step5 = riddle.increaseEnergy(step4)
    assert step5 == [
        [4,4,8,4,1,4,4,0,0,0],
        [2,0,4,4,1,4,4,0,0,0],
        [2,2,5,3,3,3,3,4,9,3],
        [1,1,5,2,3,3,3,2,7,4],
        [1,1,8,7,3,0,3,2,8,5],
        [1,1,6,4,6,3,3,2,3,3],
        [1,1,5,3,4,7,2,2,3,1],
        [6,6,4,3,3,5,2,2,3,3],
        [2,6,4,3,3,5,8,3,2,2],
        [2,2,4,3,3,4,1,3,2,2]
    ]
    """Test part 1 on example input - Step 6"""
    step6 = riddle.increaseEnergy(step5)
    assert step6 == [
        [5,5,9,5,2,5,5,1,1,1],
        [3,1,5,5,2,5,5,2,2,2],
        [3,3,6,4,4,4,4,6,0,5],
        [2,2,6,3,4,4,4,4,9,6],
        [2,2,9,8,4,1,4,3,9,6],
        [2,2,7,5,7,4,4,3,4,4],
        [2,2,6,4,5,8,3,3,4,2],
        [7,7,5,4,4,6,3,3,4,4],
        [3,7,5,4,4,6,9,4,3,3],
        [3,3,5,4,4,5,2,4,3,3]
    ]
    """Test part 1 on example input - Step 7"""
    step7 = riddle.increaseEnergy(step6)
    assert step7 == [
        [6,7,0,7,3,6,6,2,2,2],
        [4,3,7,7,3,6,6,3,3,3],
        [4,4,7,5,5,5,5,8,2,7],
        [3,4,9,6,6,5,5,7,0,9],
        [3,5,0,0,6,2,5,6,0,9],
        [3,5,0,9,9,5,5,5,6,6],
        [3,4,8,6,6,9,4,4,5,3],
        [8,8,6,5,5,8,5,5,5,5],
        [4,8,6,5,5,8,0,6,4,4],
        [4,4,6,5,5,7,4,6,4,4]
    ]    
    """Test part 1 on example input - Step 8"""
    step8 = riddle.increaseEnergy(step7)
    assert step8 == [
        [7,8,1,8,4,7,7,3,3,3],
        [5,4,8,8,4,7,7,4,4,4],
        [5,6,9,7,6,6,6,9,4,9],
        [4,6,0,8,7,6,6,8,3,0],
        [4,7,3,4,9,4,6,7,3,0],
        [4,7,4,0,0,9,7,6,8,8],
        [6,9,0,0,0,0,7,5,6,4],
        [0,0,0,0,0,0,9,6,6,6],
        [8,0,0,0,0,0,4,7,5,5],
        [6,8,0,0,0,0,7,7,5,5]
    ]
    """Test part 1 on example input - Step 9"""
    step9 = riddle.increaseEnergy(step8)
    assert step9 == [
        [9,0,6,0,0,0,0,6,4,4],
        [7,8,0,0,0,0,0,9,7,6],
        [6,9,0,0,0,0,0,0,8,0],
        [5,8,4,0,0,0,0,0,8,2],
        [5,8,5,8,0,0,0,0,9,3],
        [6,9,6,2,4,0,0,0,0,0],
        [8,0,2,1,2,5,0,0,0,9],
        [2,2,2,1,1,3,0,0,0,9],
        [9,1,1,1,1,2,8,0,9,7],
        [7,9,1,1,1,1,9,9,7,6]
    ]
    """Test part 1 on example input - Step 10"""
    step10 = riddle.increaseEnergy(step9)
    assert step10 == [
        [0,4,8,1,1,1,2,9,7,6],
        [0,0,3,1,1,1,2,0,0,9],
        [0,0,4,1,1,1,2,5,0,4],
        [0,0,8,1,1,1,1,4,0,6],
        [0,0,9,9,1,1,1,3,0,6],
        [0,0,9,3,5,1,1,2,3,3],
        [0,4,4,2,3,6,1,1,3,0],
        [5,5,3,2,2,5,2,3,5,0],
        [0,5,3,2,2,5,0,6,0,0],
        [0,0,3,2,2,4,0,0,0,0]
    ]

def test_part1_example1_10(example):
    """Test part 1 on example input with 10"""
    assert riddle.part1(example, 10) == 204

def test_part1_example1_100(example):
    """Test part 1 on example input with 10"""
    assert riddle.part1(example, 100) == 1656
    
def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example, 200) == 195