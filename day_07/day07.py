# aoc_template.py

import logging
import pathlib
import sys

class Day07:
  
  puzzle_input = None

  def __init__(self, inputFile=None):
    if (inputFile):
      logging.info(f"{inputFile}:")
      self.puzzle_input = pathlib.Path(inputFile).read_text().strip()
      logging.debug(f'Puzzle Input: {self.puzzle_input}')
    else:
      print(f'Please add Name of the inputfile to the call')
  
  def parse(self, puzzle_input):
    """Parse input"""
    ret = []
    for value in puzzle_input.split(','):
      ret.append(int(value))
    return ret

  def part1(self, data):
    """Solve part 1"""
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
        tmp = pos - i
        if (tmp<0):
          tmp *= -1
        fuel += tmp
        
        if (fuel > leastFuel):
          break

      logging.debug(f'Pos {i}: Fuel: {fuel}')
      if (fuel < leastFuel):
          leastFuel = fuel

    logging.info(f'leastFuel: {leastFuel}')

    return leastFuel

  def part2(self, data):
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
        fuel += int(tmp)
        if (fuel > leastFuel):
          break

      logging.debug(f'Pos {i}: Fuel: {fuel}')
      if (fuel < leastFuel):
          leastFuel = fuel

    return leastFuel

  def solve(self, puzzle_input=None):
    """Solve the puzzle for the given input"""
    if (puzzle_input is None):
      puzzle_input = self.puzzle_input
    data = self.parse(puzzle_input)
    logging.debug(data)
    solution1 = self.part1(data)
    solution2 = self.part2(data)

    return solution1, solution2

def main():
  logging.basicConfig(level=logging.INFO)

  sample = Day07()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()
