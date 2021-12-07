# test_day07.py

import pathlib
import pytest
import numpy as np
import day07 as day
from timeit import default_timer as timer
from datetime import timedelta

PUZZLE_DIR = pathlib.Path(__file__).parent

riddle = day.Day07()

@pytest.fixture
def example():
    puzzle_input = (PUZZLE_DIR / "example.txt").read_text().strip()
    return riddle.parse(puzzle_input)

@pytest.fixture
def input():
    #puzzle_input = np.loadtxt(PUZZLE_DIR / "input.txt", delimiter=',', dtype=np.int64)
    puzzle_input = (PUZZLE_DIR / "input.txt").read_text().strip()
    return riddle.parse(puzzle_input)

def test_parse_example(example):
    """Test that input is parsed properly"""
    assert example == [16,1,2,0,4,2,7,1,2,14]

def test_part1_example1(example):
    """Test part 1 on example input"""
    assert riddle.part1(example) == 37

def test_part2_example1(example):
    """Test part 2 on example input"""
    assert riddle.part2(example) == 168


""" Performance Tests with RealData """
def test_part2_Perf_Test_V1(input):
    """Test part 2 not optimized on real input"""
    start = timer()
    answer = part2_PerfTest_v1(input)
    end = timer()
    print(f'\nPerf V1: {timedelta(seconds=end-start)}')
    assert answer == 93214037

def test_part2_Perf_Test_V2(input):
    """Test part 2 with array optimization with numpy on real input"""
    start = timer()
    answer = part2_PerfTest_v2(input)
    end = timer()
    print(f'\nPerf V2: {timedelta(seconds=end-start)}')
    assert answer == 93214037

def test_part2_Perf_Test_V3(input):
    """Test part 2 with calc instead of loop on real input"""
    start = timer()
    answer = part2_PerfTest_v3(input)
    end = timer()
    print(f'\nPerf V3: {timedelta(seconds=end-start)}')
    assert answer == 93214037

def test_part2_Perf_Test_V4(input):
    """Test part 2 with calc instead of loop and array optimization with numpy on real input"""
    start = timer()
    answer = part2_PerfTest_v4(input)
    end = timer()
    print(f'\nPerf V4: {timedelta(seconds=end-start)}')
    assert answer == 93214037

def test_part2_Perf_Test_V5(input):
    """Test part 2 final with real input"""
    start = timer()
    answer = riddle.part2(input)
    end = timer()
    print(f'\nPerf V5: {timedelta(seconds=end-start)}')

    assert answer == 93214037

def part2_PerfTest_v1(data):
  """ Part 2 - without optimization """
  maxPos = 0
  minPos = 1000000000
  for pos in data:
    if maxPos < pos:
      maxPos = pos
    if minPos > pos:
      minPos = pos
  leastFuel = 1000000000
  for i in range(minPos, maxPos):
    fuel = 0
    for pos in data:
      distance = pos-i
      if (distance<0):
        distance *= -1
      tmp = 0
      for x in range(distance):
        tmp += x + 1
      fuel += tmp
      if (fuel > leastFuel):
        break
    if (fuel < leastFuel):
        leastFuel = fuel
  return leastFuel

def part2_PerfTest_v2(data):
  """ Perf Test with Array optimization with numpy """
  myarr = np.array(data)
  myarr = np.sort(myarr)
  unique_values, occurrence_count = np.unique(myarr, return_counts=True)
  maxPos = np.max(unique_values)
  minPos = np.min(unique_values)
  leastFuel = 1000000000
  for i in range(minPos, maxPos):
    fuel = 0
    for pos, occurrence in zip(unique_values, occurrence_count):
      distance = pos-i
      if (distance<0):
        distance *= -1
      tmp = 0
      for x in range(distance):
        tmp += x + 1
      fuel += tmp * occurrence
      if (fuel > leastFuel):
        break
    if (fuel < leastFuel):
        leastFuel = fuel
  return leastFuel

def part2_PerfTest_v3(data):
  """ Perf Test with calculation instead of loop """
  maxPos = 0
  minPos = 1000000000
  for pos in data:
    if maxPos < pos:
      maxPos = pos
    if minPos > pos:
      minPos = pos
  leastFuel = 1000000000
  for i in range(minPos, maxPos):    
    fuel = 0
    for pos in data:
      tmp = 0
      if (pos > i):
        tmp = (((pos-i) * ((pos-i) + 1))/2)
      else:
        tmp = (((i-pos) * ((i-pos) + 1))/2)
      fuel += tmp 
      if (fuel > leastFuel):
        break
    if (fuel < leastFuel):
        leastFuel = fuel
  return leastFuel

def part2_PerfTest_v4(data):
  """ Perf Test with Array optimization with numpy and optimized calc """
  myarr = np.array(data)
  myarr = np.sort(myarr)
  unique_values, occurrence_count = np.unique(myarr, return_counts=True)
  maxPos = np.max(unique_values)
  minPos = np.min(unique_values)
  leastFuel = 1000000000
  for i in range(minPos, maxPos):
    fuel = 0
    for pos, occurrence in zip(unique_values, occurrence_count):
      tmp = 0
      if (pos > i):
        tmp = (((pos-i) * ((pos-i) + 1))/2) * occurrence
      else:
        tmp = (((i-pos) * ((i-pos) + 1))/2) * occurrence
      fuel += tmp 
      if (fuel > leastFuel):
        break
    if (fuel < leastFuel):
        leastFuel = int(fuel)
  return leastFuel