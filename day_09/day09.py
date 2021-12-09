# aoc_template.py

import logging
import pathlib
import sys

class Day09:
  
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
      tmp = []
      for i in line:
        tmp.append(int(i))
      ret.append(tmp)
    return ret

  def isLowPoint(self, value, adjacent):
    ret = True
    sameCount=0
    for i in adjacent:
      if (value > i):
        ret = False
        break
      elif(value == i):
        sameCount += 1
    if (sameCount == len(adjacent)):
      ret = False
    return ret

  def findLowPoints(self, data):
    lowPoints = []
    for a in range(len(data)):
      for b in range(len(data[a])):
        # First Line
        if (a == 0):
          if (b == 0):
            logging.debug(f'{data[a][b]} ({a}/{b}) - First line / First row')
            if (self.isLowPoint(data[a][b], [ data[a][b+1], data[a+1][b]])):
              logging.debug(f'LowPoint Found: {data[a][b]}')
              lowPoints.append({'data': data[a][b], 'col': a, 'row': b})
          elif (b==len(data[a])-1):
            logging.debug(f'{data[a][b]} ({a}/{b}) - First line / Last row')
            if (self.isLowPoint(data[a][b], [ data[a][b-1], data[a+1][b]])):
              logging.debug(f'LowPoint Found: {data[a][b]}')
              lowPoints.append({'data': data[a][b], 'col': a, 'row': b})
          else:
            logging.debug(f'{data[a][b]} ({a}/{b}) - First line / Middle row')
            if (self.isLowPoint(data[a][b], [ data[a][b-1], data[a][b+1], data[a+1][b]])):
              logging.debug(f'LowPoint Found: {data[a][b]}')
              lowPoints.append({'data': data[a][b], 'col': a, 'row': b})
        elif (a==len(data)-1):
          if (b == 0):
            logging.debug(f'{data[a][b]} ({a}/{b}) - Last line / First row')
            if (self.isLowPoint(data[a][b], [ data[a][b+1], data[a-1][b]])):
              logging.debug(f'LowPoint Found: {data[a][b]}')
              lowPoints.append({'data': data[a][b], 'col': a, 'row': b})
          elif (b==len(data[a])-1):
            logging.debug(f'{data[a][b]} ({a}/{b}) - Last line / Last row')
            if (self.isLowPoint(data[a][b], [ data[a][b-1], data[a-1][b]])):
              logging.debug(f'LowPoint Found: {data[a][b]}')
              lowPoints.append({'data': data[a][b], 'col': a, 'row': b})
          else:
            logging.debug(f'{data[a][b]} ({a}/{b}) - Last line / Middle row')
            if (self.isLowPoint(data[a][b], [ data[a][b-1], data[a][b+1], data[a-1][b]])):
              logging.debug(f'LowPoint Found: {data[a][b]}')
              lowPoints.append({'data': data[a][b], 'col': a, 'row': b})
        else:
          if (b == 0):
            logging.debug(f'{data[a][b]} ({a}/{b}) - Middle line / First row')
            if (self.isLowPoint(data[a][b], [ data[a][b+1], data[a-1][b], data[a+1][b]])):
              logging.debug(f'LowPoint Found: {data[a][b]}')
              lowPoints.append({'data': data[a][b], 'col': a, 'row': b})
          elif (b==len(data[a])-1):
            logging.debug(f'{data[a][b]} ({a}/{b}) - Middle line / Last row')
            if (self.isLowPoint(data[a][b], [ data[a][b-1], data[a-1][b], data[a+1][b]])):
              logging.debug(f'LowPoint Found: {data[a][b]}')
              lowPoints.append({'data': data[a][b], 'col': a, 'row': b})
          else:
            logging.debug(f'{data[a][b]} ({a}/{b}) - Middle line / Middle row')
            if (self.isLowPoint(data[a][b], [ data[a][b-1], data[a][b+1], data[a-1][b], data[a+1][b]])):
              logging.debug(f'LowPoint Found: {data[a][b]}')
              lowPoints.append({'data': data[a][b], 'col': a, 'row': b})

    return lowPoints

  def part1(self, data):
    """Solve part 1"""
    ret = 0
    lowPoints = self.findLowPoints(data)
    for i in lowPoints:
      ret += 1 + i['data']
    return ret

  def initSearchArray(self, row, col):
    ret = []
    for a in range(row):
      line = []
      for b in range(col):
        line.append(0)
      ret.append(line)
    return ret

  def searchLeft(self, a, b, data, found):
    for i in range(b, -1, -1):
      logging.debug(f'<: {data[a][i]}')
      if(data[a][i] == 9 or data[a][i] == 1):
        break
      else:
        found[a][i] = 1
        self.searchUp(a-1, i, data, found)
        self.searchDown(a+1, i, data, found)

  def searchRight(self, a, b, data, found):
    for i in range(b, len(data[a]), +1):
      logging.debug(f'>: {data[a][i]}')
      if(data[a][i] == 9 or found[a][i] == 1):
        break
      else:
        found[a][i] = 1
        self.searchUp(a-1, i, data, found)
        self.searchDown(a+1, i, data, found)

  def searchUp(self, a, b, data, found):
    for i in range(a, -1, -1):
      logging.debug(f'^: {data[i][b]}')
      if(data[i][b] == 9 or found[i][b] == 1):
        break
      else:
        found[i][b] = 1
        self.searchLeft(i, b-1, data, found)
        self.searchRight(i, b+1, data, found)

  def searchDown(self, a, b, data, found):
    for i in range(a, len(data), +1):
      logging.debug(f'v: {data[i][b]}')
      if(data[i][b] == 9 or found[i][b] == 1):
        break
      else:
        found[i][b] = 1
        self.searchLeft(i, b-1, data, found)
        self.searchRight(i, b+1, data, found)

  def searchBasin(self, pos, data, found):
    a = pos['col']
    b = pos['row']
    logging.debug(f'{data[a][b]} ({a}/{b})')
    found[a][b] = 1

    self.searchLeft(a, b-1, data, found)
    self.searchRight(a, b+1, data, found)
    self.searchUp(a-1, b, data, found)
    self.searchDown(a+1, b, data, found)

    for line in found:
      logging.debug(f'{line}')


  def countBasin(self, pos, data):
    ret = 0
    found = self.initSearchArray(len(data), len(data[0]))
    self.searchBasin(pos, data, found)
    for a in range(len(found)):
      for b in range(len(found[0])):
        ret += found[a][b]
    return ret

  def part2(self, data):
    """Solve part 2"""
    ret = 1
    lowPoints = self.findLowPoints(data)
    
    counter = []
    for i in lowPoints:
      tmp = self.countBasin(i, data)
      counter.append(tmp)
      logging.debug(f'counter: {tmp}')

    counter.sort(reverse=True)
    logging.debug (counter)
    for i in range(3):
      ret *= counter[i]
    return ret

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

  sample = Day09()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()
