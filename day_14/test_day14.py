# test_day14.py

import pathlib
import pytest
import day14 as day

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day14()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example[0] == 'NNCB'
    """
    assert example[1] == {
        'CH': 'B',
        'HH': 'N', 
        'CB': 'H', 
        'NH': 'C', 
        'HB': 'C', 
        'HC': 'B', 
        'HN': 'C', 
        'NN': 'C', 
        'BH': 'H', 
        'NC': 'B', 
        'NB': 'B', 
        'BN': 'B', 
        'BB': 'N', 
        'BC': 'B', 
        'CC': 'N', 
        'CN': 'C'
    }
    """
    assert example[1] =={
        ('C', 'H'): 'B', 
        ('H', 'H'): 'N', 
        ('C', 'B'): 'H', 
        ('N', 'H'): 'C', 
        ('H', 'B'): 'C', 
        ('H', 'C'): 'B', 
        ('H', 'N'): 'C', 
        ('N', 'N'): 'C', 
        ('B', 'H'): 'H', 
        ('N', 'C'): 'B', 
        ('N', 'B'): 'B', 
        ('B', 'N'): 'B', 
        ('B', 'B'): 'N', 
        ('B', 'C'): 'B', 
        ('C', 'C'): 'N', 
        ('C', 'N'): 'C'
    }

@pytest.mark.skip(reason="Refactored, not neccesary anymore")
def test_applyRules(example):
    """Test applyRules on example input"""
    rules = example[1]
    step1 = riddle.applyRules(example[0], rules)
    assert step1 == 'NCNBCHB'
    step2 = riddle.applyRules(step1, rules)
    assert step2 == 'NBCCNBBBCBHCB'
    step3 = riddle.applyRules(step2, rules)
    assert step3 == 'NBBBCNCCNBBNBNBBCHBHHBCHB'
    step4 = riddle.applyRules(step3, rules)
    assert step4 == 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'

def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example, 10) == 1588
    
def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example, 40) == 2188189693529

    