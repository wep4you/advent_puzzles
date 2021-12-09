# day.py

import logging
import pathlib
import sys

class Day10:
  
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

  def part1(self, data):
    """Solve part 1"""

  def part2(self, data):
    """Solve part 2"""

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

  sample = Day10()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()
