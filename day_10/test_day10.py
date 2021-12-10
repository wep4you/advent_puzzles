# test_day10.py

import pathlib
import pytest
import day10 as day

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day10()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [
        '[({(<(())[]>[[{[]{<()<>>',
        '[(()[<>])]({[<{<<[]>>(',
        '{([(<{}[<>[]}>{[]{[(<()>',
        '(((({<>}<{<{<>}{[]{[]{}',
        '[[<[([]))<([[{}[[()]]]',
        '[{[{({}]{}}([{[{{{}}([]',
        '{<[[]]>}<{[{[{[]{()[[[]',
        '[<(<(<(<{}))><([]([]()',
        '<{([([[(<>()){}]>(<<{{',
        '<{([{{}}[<[[[<>{}]]]>[]]'
    ]

def test_findCorrupted():
    """Test find corrupted Lines example input"""
    assert riddle.findCorrupted('{([(<{}[<>[]}>{[]{[(<()>') == '}'
    assert riddle.findCorrupted('[[<[([]))<([[{}[[()]]]') == ')'
    assert riddle.findCorrupted('[{[{({}]{}}([{[{{{}}([]') == ']'
    assert riddle.findCorrupted('[<(<(<(<{}))><([]([]()') == ')'
    assert riddle.findCorrupted('<{([([[(<>()){}]>(<<{{') == '>'

def test_findNotCorrupted():
    """Test find corrupted Lines example input"""
    assert riddle.findCorrupted('[({(<(())[]>[[{[]{<()<>>')[0] == None
    assert riddle.findCorrupted('[(()[<>])]({[<{<<[]>>(')[0] == None
    assert riddle.findCorrupted('(((({<>}<{<{<>}{[]{[]{}')[0] == None
    assert riddle.findCorrupted('{<[[]]>}<{[{[{[]{()[[[]')[0] == None
    assert riddle.findCorrupted('<{([{{}}[<[[[<>{}]]]>[]]')[0] == None

def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example) == 26397

def test_Autocomplete():
    """Test Autocomplete Lines example input"""
    val = riddle.findCorrupted('[({(<(())[]>[[{[]{<()<>>')
    assert riddle.autoComplete(val[1]) == ['}','}',']',']',')','}',')',']']

    val = riddle.findCorrupted('[(()[<>])]({[<{<<[]>>(')
    assert riddle.autoComplete(val[1]) == [')','}','>',']','}',')']

    val = riddle.findCorrupted('(((({<>}<{<{<>}{[]{[]{}')
    assert riddle.autoComplete(val[1]) == ['}','}','>','}','>',')',')',')',')']

    val = riddle.findCorrupted('{<[[]]>}<{[{[{[]{()[[[]')
    assert riddle.autoComplete(val[1]) == [']',']','}','}',']','}',']','}','>']

    val = riddle.findCorrupted('<{([{{}}[<[[[<>{}]]]>[]]')
    assert riddle.autoComplete(val[1]) == [']',')','}','>']

def test_CalculateAutocomplete():
    """Test Autocomplete Lines example input"""
    assert riddle.calcAutoComplete(['}','}',']',']',')','}',')',']']) == 288957
    assert riddle.calcAutoComplete([')','}','>',']','}',')']) == 5566
    assert riddle.calcAutoComplete(['}','}','>','}','>',')',')',')',')']) == 1480781
    assert riddle.calcAutoComplete([']',']','}','}',']','}',']','}','>']) == 995444
    assert riddle.calcAutoComplete([']',')','}','>']) == 294

def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example) == 288957