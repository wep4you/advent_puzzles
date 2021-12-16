# day.py

import logging
import pathlib
from re import X
import sys
import timeit
import numpy as np

from collections import Counter, defaultdict
from itertools import pairwise

class Day14:
  
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
    input_parts = puzzle_input.split('\n\n')
    logging.debug(f'{input_parts}')
    polymer = input_parts[0]
    pairRules = {}
    for values in input_parts[1].split('\n'):
      value = values.split(' -> ')
      pairRules[(value[0][0], value[0][1])] = value[1]

    logging.debug(f'PolimerInput: {polymer} ')
    logging.debug(f'Pair rules: {pairRules}')

    return polymer, pairRules    

  def part1(self, data, steps=10):
    """Solve part 1"""
    return self.part2(data, steps)

  def part2(self, data, steps=10):
    pair_count = Counter(pairwise(data[0]))
    logging.debug(f'{pair_count}')
    polymer_count = defaultdict(lambda: 0, Counter(data[0]))
    logging.debug(f'{polymer_count}')
    rules = data[1]

    for i in range(steps):
      temp_pair_count: dict[tuple[str, str], int] = defaultdict(lambda: 0)
      logging.debug(f'---')
      for (a, b), count in pair_count.items():
        x = rules[a, b]
        polymer_count[x] += count
        logging.debug(f'({a},{b}) <- {x} + {count}')
        temp_pair_count[a, x] += count
        temp_pair_count[x, b] += count
        logging.debug(f'({a},{x}) + {count} | ({x},{b}) + {count}')
      pair_count = temp_pair_count
      logging.debug(f'pair_count: {pair_count}')
      logging.debug(f'-- {polymer_count} --')

    minVal = min(polymer_count.values())
    maxVal = max(polymer_count.values())
    solution = maxVal - minVal
    logging.info(f'Answer: {solution}: min={minVal} max={maxVal}')

    return solution

  """
  Different approaches, for Part 2, which didn't work as expected,
  but leave it here for documentation

  START
  """
  def recursiveRules(self, iteration, key, input, rules, depth):
    if(iteration in (range(5))):
      print(f'iteration: {iteration} - key: {key}')
    if (not key in input):
      counter = [0] * (iteration+1)
      counter[iteration] += 1
      input[key] = {
        'value': key[0],
        'left': ''.join([key[0], rules[key]]),
        'right': ''.join([rules[key], key[1]]),
        'count': counter
      }
      logging.debug(f'\nNew Root Node: {input}')
    else:
      rootCount = input[key].get('count')
      if(len(rootCount) > iteration ):
        rootCount[iteration] += 1
      else:
        for i in range(iteration+1 - len(rootCount)):
          rootCount.append(0)
        rootCount[iteration] += 1

    iteration += 1
    logging.debug(f'iter: {iteration} / depth: {depth}')
    if (iteration < depth):
      leftVal = input[key].get('left')
      input = self.recursiveRules(iteration, leftVal, input, rules, depth)
      logging.debug(f'\nLeft: {input}')
      rightVal = input[key].get('right')
      input = self.recursiveRules(iteration, rightVal, input, rules, depth)
      logging.debug(f'\nRight: {input}')
    iteration -= 1

    return input      
    
  def applyRules(self, inPolymer, rules):
    newPolymer = []
    for i in range(len(inPolymer)):
      part = inPolymer[i:i+2]
      if (len(part) == 2):
        newPolymer.append(''.join([part[0], rules.get(part)]))
        logging.debug(f'{i}: {part}')
      else:
         newPolymer.append(part[0])

    logging.debug(f'{newPolymer}')
    return ''.join(newPolymer)

  def part1_initial(self, data, steps=10):
    """Solve part 1"""
    inPolymer = data[0]
    rules = data[1]

    polymer = inPolymer
    for i in range(steps):
      logging.debug(i)
      start = timeit.default_timer()
      
      polymer = self.applyRules(polymer, rules)
      
      stop = timeit.default_timer()
      logging.debug(f'{i}: {stop - start}')

    npPolymer = np.array(list(polymer))
    logging.debug(f'{npPolymer} ({npPolymer.shape})')

    unique, counts = np.unique(npPolymer, return_counts=True)
    sums = dict(zip(unique, counts))

    minVal = min(sums.values())
    maxVal = max(sums.values())
    ret = maxVal - minVal

    logging.debug(f'min {minVal} - max {maxVal} - diff: {ret} - ({sums})')

    return ret
  """
  END
  """

  def solve(self, puzzle_input=None):
    """Solve the puzzle for the given input"""
    if (puzzle_input is None):
      puzzle_input = self.puzzle_input
    data = self.parse(puzzle_input)
    logging.debug(data)
    solution1 = self.part1(data, 10)
    solution2 = self.part2(data, 40)

    return solution1, solution2

def main():
  logging.basicConfig(level=logging.INFO)

  sample = Day14()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()
