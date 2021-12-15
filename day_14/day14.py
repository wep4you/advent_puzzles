# day.py

import logging
import pathlib
from re import X
import sys
import timeit
import numpy as np

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
      pairRules[value[0]] = value[1]

    logging.debug(f'PolimerInput: {polymer} ')
    logging.debug(f'Pair rules: {pairRules}')

    return polymer, pairRules    



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



  def part1(self, data, steps=10):
    """Solve part 1"""
    inPolymer = data[0]
    rules = data[1]

    polymer = inPolymer
    for i in range(steps):
      logging.debug(i)
      start = timeit.default_timer()
      
      polymer = self.applyRules(polymer, rules)
      
      stop = timeit.default_timer()
      print(f'{i}: {stop - start}')

    npPolymer = np.array(list(polymer))
    logging.debug(f'{npPolymer} ({npPolymer.shape})')

    unique, counts = np.unique(npPolymer, return_counts=True)
    sums = dict(zip(unique, counts))

    minVal = min(sums.values())
    maxVal = max(sums.values())
    ret = maxVal - minVal

    logging.debug(f'min {minVal} - max {maxVal} - diff: {ret} - ({sums})')

    return ret

  def part2_recursive(self, data, steps=20):
    """Solve part 2"""
    functionStart = timeit.default_timer()

    steps += 1
    input = data[0]
    rules = data[1]

    ret = {}
    for i in range(len(input)-1):
      start = timeit.default_timer()
      val = input[i:i+2]
      ret = self.recursiveRules(0, val, ret, rules, steps)

      stop = timeit.default_timer()
      print(f'{val}: {stop - start}')
      
    logging.debug(f'--- {ret}')
    x = {input[-1]: 1}
    for key in ret:
      val = ret[key].get("value")
      countArr = ret[key].get("count")
      count = 0
      if(len(countArr)>=steps):
        count = countArr[steps-1]
      logging.debug(f'{key}: {val} - {count}')

      if (val in x):
        x[val] += count
      else:
        x[val] = count

    maxVal = max(x.values())
    minVal = min(x.values())

    functionStop = timeit.default_timer()

    print(f'min: {minVal} - max: {maxVal} - {functionStop - functionStart} - ({x})')

    return maxVal-minVal



  def initDict(self, values):
    ret = {}
    for value in values:
      ret[value] = {}

    return ret



  def part2(self, data, steps=10):
    inPolymer = data[0]
    rules = data[1]
   
    # Calculate all possible values and calculate for half of the needed steps
    sums = self.initDict(rules.keys())
    print(f'initDict: {sums}')

    for keys in sums.keys():
      input = keys
      for i in range(int(steps/2)):
        input = self.applyRules(input, rules)

      npPolymer = np.array(list(input))
      unique, counts = np.unique(npPolymer, return_counts=True)
      calcSums = dict(zip(unique, counts))

      sums[keys] = calcSums
    print(f'{sums}')

    # Now use the inputValues to get the String on Pos Array/2
    polymer = inPolymer
    for i in range(int(steps/2)):
      polymer = self.applyRules(polymer, rules)
    print(f'{polymer}')

    solution = {}
    # Calculate Sums with polymor on Postion Step/2 with calculated values 
    for i in range(len(polymer)):
      keyPoly = polymer[i:i+2]
      print(f'keyPoly: {keyPoly}')
      if(keyPoly in sums):
        for key in sums[keyPoly].keys():
          print(f'{key} : {sums[keyPoly][key]}')
          #if(key != keyPoly[-1]):
          if (key in solution):
            solution[key] += sums[keyPoly][key]
          else:
            solution[key] = sums[keyPoly][key]

    #solution[polymer[-1]] += 1
    print(f'solution: {solution}')



      #minVal = min(sums.values())
      #maxVal = max(sums.values())
      #ret = maxVal - minVal


  def solve(self, puzzle_input=None):
    """Solve the puzzle for the given input"""
    if (puzzle_input is None):
      puzzle_input = self.puzzle_input
    data = self.parse(puzzle_input)
    logging.debug(data)
    solution1 = self.part1(data)
    solution2 = self.part2_recursive(data, 40)

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
