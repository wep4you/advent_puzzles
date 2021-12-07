import logging
import pathlib
import sys

class Day06:
  
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
    for line in puzzle_input.split():
      values = line.split(',')
      for value in values:
        ret.append(int(value))
      logging.debug(ret)
    return ret

  def part1(self, data, dayCount):
    """Solve part 1"""
    input = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
    for i in range(len(data)):
      input[data[i]] += 1

    fishAges = input
    for i in range (dayCount):
      tmpfishAges = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
      for key in fishAges:
        if (key == 0):
          tmpfishAges[8] += fishAges[key]
          tmpfishAges[6] += fishAges[key]
        else:
          tmpfishAges[key-1] += fishAges[key]
      fishAges = tmpfishAges
      logging.debug(f'Day {i+1}: {fishAges}')
    logging.info(f'Day {i+1}: {fishAges}')

    fishCount = 0
    for key in fishAges:
      fishCount += fishAges[key]

    return fishCount

  def part2(self, data, dayCount):
    """Solve part 2"""
    return self.part1(data, dayCount)

  def solve(self, puzzle_input=None):
    """Solve the puzzle for the given input"""
    if (puzzle_input is None):
      puzzle_input = self.puzzle_input
    data = self.parse(puzzle_input)
    logging.debug(data)
    solution1 = self.part1(data, 80)
    solution2 = self.part2(data, 256)

    return solution1, solution2


def main():
  logging.basicConfig(level=logging.DEBUG)

  sample = Day06()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()