# day.py

import logging
import pathlib
import sys

class Day11:
  
  puzzle_input = None
  flashCount = 0

  def __init__(self, inputFile=None):
    if (inputFile):
      #logging.info(f"{inputFile}:")
      self.puzzle_input = pathlib.Path(inputFile).read_text().strip()
      logging.debug(f'Puzzle Input: {self.puzzle_input}')
    else:
      print(f'Please add Name of the inputfile to the call')
  
  def parse(self, puzzle_input):
    """Parse input"""
    ret = []
    for line in puzzle_input.split():
      values = []
      for i, val in enumerate(line):
        values.append(int(val))
      ret.append(values)
    return ret

  def incW(self, posA, posB, data):
    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'in - incW: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    a = posA
    b = posB - 1
    if (b >= 0):
      logging.debug(f' <: {data[a][b]} ({a}/{b})')
      if(data[a][b] < 10):
        data[a][b] += 1        
        if(data[a][b] == 10):
          self.flash(a, b, data)

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'out - incW: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')          

  def incE(self, posA, posB, data):
    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'in - incE: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    a = posA
    b = posB + 1
    if (b < len(data[0])):
      logging.debug(f' >: {data[a][b]} ({a}/{b})')
      if(data[a][b] < 10):
        data[a][b] += 1
        if(data[a][b] == 10):
          self.flash(a, b, data)

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'out - incE: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')          

  def incN(self, posA, posB, data):
    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'in - incN: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    a = posA - 1
    b = posB
    if (a >= 0):
      logging.debug(f'^ : {data[a][b]} ({a}/{b})')
      if(data[a][b] < 10):
        data[a][b] += 1
        if(data[a][b] == 10):
          self.flash(a, b, data)

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'out - incN: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')          

  def incS(self, posA, posB, data):
    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'in - incS: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    a = posA + 1
    b = posB
    if (a < len(data)):
      logging.debug(f'v : {data[a][b]} ({a}/{b})')
      if(data[a][b] < 10):
        data[a][b] += 1
        if(data[a][b] == 10):
          self.flash(a, b, data)

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'out - incS: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

  def incNW(self, posA, posB, data):
    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'in - incNW: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    a = posA - 1
    b = posB - 1 
    if (a >= 0 and b >= 0):
      logging.debug(f'^<: {data[a][b]} ({a}/{b})')
      if(data[a][b] < 10):
        data[a][b] += 1
        if(data[a][b] == 10):
          self.flash(a, b, data)

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'out - incNW: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')          

  def incNE(self, posA, posB, data):
    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'in - incNE: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    a = posA - 1
    b = posB + 1
    if (a >= 0 and b < len(data[0])):
      logging.debug(f'^>: {data[a][b]} ({a}/{b})')
      if(data[a][b] < 10):
        data[a][b] += 1
        if(data[a][b] == 10):
          self.flash(a, b, data)

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'out - incNE: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

  def incSW(self, posA, posB, data):
    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'in - incSW: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    a = posA + 1
    b = posB - 1
    if (a < len(data) and b >= 0):
      logging.debug(f'v : {data[a][b]} ({a}/{b})')
      if(data[a][b] < 10):
        data[a][b] += 1
        if(data[a][b] == 10):
          self.flash(a, b, data)

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'out - incSW: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')          

  def incSE(self, posA, posB, data):
    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'in - incSE: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    a = posA + 1
    b = posB + 1
    if (a < len(data) and b < len(data[0])):
      logging.debug(f'v : {data[a][b]} ({a}/{b})')
      if(data[a][b] < 10):
        data[a][b] += 1
        if(data[a][b] == 10):
          self.flash(a, b, data)

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'out - incSE: ({posA},{posB})')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

  def flash(self, a, b, data):
    if(data[a][b] == 10):
      logging.debug(f'-- Flash ({a},{b})--')
      self.flashCount += 1

      if logging.getLogger().level == logging.DEBUG:
        for i in range(len(data)):
          logging.debug(f'{data[i]}')

      self.incNW(a, b, data)
      self.incN(a, b, data)
      self.incNE(a, b, data)
      self.incW(a, b, data)
      self.incE(a, b, data)
      self.incSW(a, b, data)
      self.incS(a, b, data)
      self.incSE(a, b, data)

  def increaseEnergy(self, data):
    logging.debug(f'--- New Data Set - increaseEnergy ---')
    countFlash = 0

    for a in range(len(data)):
      for b in range(len(data[a])):
        if(data[a][b] < 10):
          data[a][b] += 1

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'After 1. increase')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    toFlash = []
    for a in range(len(data)):
      for b in range(len(data[a])):
        if(data[a][b] == 10):
          toFlash.append({'a': a, 'b': b})

    if logging.getLogger().level == logging.DEBUG:
      for coord in toFlash:
        logging.debug(f'To flash: {coord}')

    for coord in toFlash:
      self.flash(coord['a'], coord['b'], data)

    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'After Flash')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    for a in range(len(data)):
      for b in range(len(data[a])):
        if(data[a][b] == 10):
          data[a][b] = 0
    
    if logging.getLogger().level == logging.DEBUG:
      logging.debug(f'After Energy reduced')
      for i in range(len(data)):
        logging.debug(f'{data[i]}')

    return data

  def part1(self, data, iter=100):
    """Solve part 1"""
    self.flashCount = 0
    for i in range (iter):
      self.increaseEnergy(data)
    return self.flashCount

  def part2(self, data, iter=500):
    """Solve part 2"""
    logging.basicConfig(level=logging.DEBUG)

    ret = 0
    for i in range (iter):
      logging.debug(f'{i} -----------------------------')
      self.increaseEnergy(data)

      for x in range(len(data)):
        logging.debug(f'{data[x]}')

      allFlash = True
      for line in data:
        for val in line:
          if (val != 0):
            allFlash = False
            break
        if (allFlash == False):
          break

      if (allFlash):
        logging.debug(f'Synchron: {i}')
        ret = i+1
        break
    return ret

  def solve(self, puzzle_input=None):
    """Solve the puzzle for the given input"""
    if (puzzle_input is None):
      puzzle_input = self.puzzle_input
    data = self.parse(puzzle_input)
    logging.debug(data)
    solution1 = self.part1(data)

    data = self.parse(puzzle_input)
    solution2 = self.part2(data)

    return solution1, solution2


def main():
  logging.basicConfig(level=logging.INFO)

  sample = Day11()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()
