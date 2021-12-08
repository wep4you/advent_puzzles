# test_day09.py

import pathlib
import pytest
import day08 as day
import logging

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day08()
logging.basicConfig(level=logging.DEBUG)

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return riddle.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        [['acedgfb','cdfbe','gcdfa','fbcad','dab','cefabd','cdfgeb','eafb','cagedb','ab'], ['cdfeb','fcadb','cdfeb','cdbaf']]
    ]

def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert example2 == [
        [['be','cfbegad','cbdgef','fgaecd','cgeb','fdcge','agebfd','fecdb','fabcd','edb'], ['fdgacbe','cefdb','cefbgd','gcbe']],
        [['edbfga','begcd','cbg','gc','gcadebf','fbgde','acbgfd','abcde','gfcbed','gfec'], ['fcgedb','cgb','dgebacf','gc']],
        [['fgaebd','cg','bdaec','gdafb','agbcfd','gdcbef','bgcad','gfac','gcb','cdgabef'], ['cg','cg','fdcagb','cbg']],
        [['fbegcd','cbd','adcefb','dageb','afcb','bc','aefdc','ecdab','fgdeca','fcdbega'], ['efabcd','cedba','gadfec','cb']],
        [['aecbfdg','fbg','gf','bafeg','dbefa','fcge','gcbea','fcaegb','dgceab','fcbdga'], ['gecf','egdcabf','bgf','bfgea']],
        [['fgeab','ca','afcebg','bdacfeg','cfaedg','gcfdb','baec','bfadeg','bafgc','acf'], ['gebdcfa','ecba','ca','fadegcb']],
        [['dbcfg','fgd','bdegcaf','fgec','aegbdf','ecdfab','fbedc','dacgb','gdcebf','gf'], ['cefg','dcbef','fcge','gbcadfe']],
        [['bdfegc','cbegaf','gecbf','dfcage','bdacg','ed','bedf','ced','adcbefg','gebcd'], ['ed','bcgafe','cdgba','cbgef']],
        [['egadfb','cdbfeg','cegd','fecab','cgb','gbdefca','cg','fgcdab','egfdb','bfceg'], ['gbdfcae','bgc','cg','cgb']],
        [['gcafb','gcf','dcaebfg','ecagb','gf','abcdeg','gaef','cafbge','fdbac','fegbdc'], ['fgae','cfgab','fg','bagce']]
    ]

@pytest.mark.skip(reason="Test just one other")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert riddle.part1(example1) == 0

@pytest.mark.skip(reason="Test just one other")
def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert riddle.part1({example2}) == 26

def test_part2_analyzeInput_Simple(example1):
    """Test analyzeInput_Simple with example input"""
    code = riddle.analyzeInput(example1[0][0])
    assert 'acedgfb' == code[8]
    assert 'cdfbe' == code[5]
    assert 'gcdfa' == code[2]
    assert 'fbcad' == code[3]
    assert 'dab' == code[7]
    assert 'cefabd' == code[9]
    assert 'cdfgeb' == code[6]
    assert 'eafb' == code[4]
    assert 'cagedb' == code[0]
    assert 'ab' == code[1]    

def test_part2_example2_line0(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[0][0])
    lineSum = riddle.calculateOut(example2[0][1], code)
    assert lineSum == 8394

def test_part2_example2_line1(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[1][0])
    lineSum = riddle.calculateOut(example2[1][1], code)
    assert lineSum == 9781

def test_part2_example2_line2(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[2][0])
    lineSum = riddle.calculateOut(example2[2][1], code)
    assert lineSum == 1197

def test_part2_example2_line3(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[3][0])
    lineSum = riddle.calculateOut(example2[3][1], code)
    assert lineSum == 9361

def test_part2_example2_line4(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[4][0])
    lineSum = riddle.calculateOut(example2[4][1], code)
    assert lineSum == 4873

def test_part2_example2_line5(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[5][0])
    lineSum = riddle.calculateOut(example2[5][1], code)
    assert lineSum == 8418

def test_part2_example2_line6(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[6][0])
    lineSum = riddle.calculateOut(example2[6][1], code)
    assert lineSum == 4548

def test_part2_example2_line7(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[7][0])
    lineSum = riddle.calculateOut(example2[7][1], code)
    assert lineSum == 1625

def test_part2_example2_line8(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[8][0])
    lineSum = riddle.calculateOut(example2[8][1], code)
    assert lineSum == 8717

def test_part2_example2_line9(example2):
    """Test part 2 on example input"""
    code = riddle.analyzeInput(example2[9][0])
    lineSum = riddle.calculateOut(example2[9][1], code)
    assert lineSum == 4315

def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert riddle.part2(example1) == 5353

def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert riddle.part2(example2) == 61229