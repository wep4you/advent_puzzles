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

@pytest.mark.skip(reason="Not implemented")
def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example[0] == 'NNCB'
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

@pytest.mark.skip(reason="Not implemented")
def test_recursiveRules_1(example):
    """Test applyRules on example input"""
    rules = example[1]
    input = {}
    step1 = riddle.recursiveRules(0, 'NN', input, rules, 1)
    assert step1 == {
        'NN': {'value': 'N', 'left': 'NC', 'right': 'CN', 'count': [1]}
    }

@pytest.mark.skip(reason="Not implemented")
def test_recursiveRules_2(example):
    rules = example[1]
    input = {}
    step2 = riddle.recursiveRules(0, 'NN', input, rules, 2)
    assert step2 == {
        'NN': {'value': 'N', 'left': 'NC', 'right': 'CN', 'count': [1]}, 
        'NC': {'value': 'N', 'left': 'NB', 'right': 'BC', 'count': [0, 1]}, 
        'CN': {'value': 'C', 'left': 'CC', 'right': 'CN', 'count': [0, 1]}, 
    }

@pytest.mark.skip(reason="Not implemented")
def test_recursiveRules_3(example):
    rules = example[1]
    input = {}
    step2 = riddle.recursiveRules(0, 'NN', input, rules, 3)
    assert step2 == {
        'NN': {'value': 'N', 'left': 'NC', 'right': 'CN', 'count': [1]}, 
        'NC': {'value': 'N', 'left': 'NB', 'right': 'BC', 'count': [0, 1]}, 
        'CN': {'value': 'C', 'left': 'CC', 'right': 'CN', 'count': [0, 1, 1]}, 
        'NB': {'value': 'N', 'left': 'NB', 'right': 'BB', 'count': [0, 0, 1]}, 
        'BC': {'value': 'B', 'left': 'BB', 'right': 'BC', 'count': [0, 0, 1]}, 
        'CC': {'value': 'C', 'left': 'CN', 'right': 'NC', 'count': [0, 0, 1]}
    }

@pytest.mark.skip(reason="Not implemented")
def test_recursiveRules_4(example):
    rules = example[1]
    input = {}
    step2 = riddle.recursiveRules(0, 'NN', input, rules, 4)
    assert step2 == {
        'NN': {'value': 'N', 'left': 'NC', 'right': 'CN', 'count': [1]}, 
        'NC': {'value': 'N', 'left': 'NB', 'right': 'BC', 'count': [0, 1, 1]}, 
        'NB': {'value': 'N', 'left': 'NB', 'right': 'BB', 'count': [0, 0, 1, 1]}, 
        'BB': {'value': 'B', 'left': 'BN', 'right': 'NB', 'count': [0, 0, 0, 2]}, 
        'BC': {'value': 'B', 'left': 'BB', 'right': 'BC', 'count': [0, 0, 1, 1]}, 
        'CN': {'value': 'C', 'left': 'CC', 'right': 'CN', 'count': [0, 1, 2, 1]}, 
        'CC': {'value': 'C', 'left': 'CN', 'right': 'NC', 'count': [0, 0, 1, 1]}
    }

@pytest.mark.skip(reason="Not implemented")
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

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example, 10) == 1588
    
@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example) == 2188189693529

def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2_recursive(example,10) == 1588
    