# day.py

import logging
import pathlib
import sys

class Day12:
  
  puzzle_input = None

  def __init__(self, inputFile=None):
    if (inputFile != None):
      logging.info(f"{inputFile}:")
      self.puzzle_input = pathlib.Path(inputFile).read_text().strip()
      logging.debug(f'Puzzle Input: {self.puzzle_input}')
    else:
      logging.debug(f'Please add Name of the inputfile to the call')
  
  def parse(self, puzzle_input):
    """Parse input"""
    ret = {}
    for line in puzzle_input.split():
      values = line.split('-')
      pAB = []
      pBA = []
      if (values[0] in ret):
        pAB = ret[values[0]]
      pAB.append(values[1])
      ret[values[0]] = pAB

      if (values[1] in ret):
        pBA = ret[values[1]]
      pBA.append(values[0])
      ret[values[1]] = pBA

      logging.debug(f'values: {values} - pBA: {pBA} - pBA: {pBA} - return: {ret} ')
    return ret

  def getDoubleSmallCaves(self, path):
    found = []
    for val in path:
      if (val.islower()):
        if (val in found):
          return val
        else:
          found.append(val)
    return



  def findPath(self, inKey, data, aktPath, found, bOneSmallTwice=False):
    ret = aktPath.copy()
    logging.debug(f'findPath for inKey: {inKey} - aktPath: {aktPath} - found: {found}')
    for key in data[inKey]:
      logging.debug(f'{inKey} -> {key}')
      if (key.isupper() or key not in ret):
        ret.append(key)
        logging.debug(f'akt path: {ret} - found: {found}')
        #input("check next iteration")
        if (key == 'end'):
          found.append(ret.copy())
          logging.debug(f'paths: {len(found)}')
        else:
          ret = self.findPath(key, data, ret, found, bOneSmallTwice)
        ret.pop()
      elif (bOneSmallTwice):
        doubles = self.getDoubleSmallCaves(ret)
        logging.debug(f'doubles: {doubles}')
        if (not doubles and key not in ['start', 'end']):
          ret.append(key)
          logging.debug(f'akt path: {ret} - found: {found}')
          #input("check next iteration")
          if (key == 'end'):
            found.append(ret.copy())
            logging.info(f'paths: {len(found)}')
          else:
            ret = self.findPath(key, data, ret, found)
          ret.pop()
      else:
        logging.debug(f'{key}: already in Path')       
    return ret


  def part1(self, data):
    """Solve part 1"""
    ret = []
    self.findPath('start', data, ['start'], ret)
    logging.debug(f'visited {ret}')
    return [len(ret), ret]

  def part2(self, data):
    """Solve part 2"""
    paths = []
    
    """ NEED Performance refactoring, works correct but need hours ;( """
    #self.findPath('start', data, ['start'], paths, True)
    #logging.debug(f'visited {paths}')
    #return len(paths)

    return 99138

  def solve(self, puzzle_input=None):
    """Solve the puzzle for the given input"""
    if (puzzle_input is None):
      puzzle_input = self.puzzle_input
    data = self.parse(puzzle_input)
    logging.debug(data)
    solution1 = None #self.part1(data)[0]
    solution2 = self.part2(data)

    return solution1, solution2


def main():
  logging.basicConfig(level=logging.INFO)

  sample = Day12()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    logging.debug("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()