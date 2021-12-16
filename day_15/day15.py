# day.py

import logging
import pathlib
import sys
import numpy as np

class Day15:
  
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
      lineArray = []
      for i,val in enumerate(line):
        lineArray.append(int(val))
      ret.append(lineArray)
    return np.array(ret)

  def right(self, risk, data, visited, row, col, found):
    col += 1
    if (col in range(data.shape[1]) and visited[row,col] == 0):
      risk += data[row, col]
      visited[row, col] = 1
      if(row==data.shape[0]-1 and col==data.shape[1]-1):
        if(risk < found[-1]):
          logging.info(f'New Path found: {risk}')
          found.append(risk)
      elif(risk < found[-1]):
        self.down(risk, data, visited, row, col, found)
        self.up(risk, data, visited, row, col, found)
        self.right(risk, data, visited, row, col, found)
      visited[row, col] = 0
    col -= 1
    return risk

  def left(self, risk, data, visited, row, col, found):
    col -= 1
    if (col in range(data.shape[1]) and visited[row,col] == 0):
      risk += data[row, col]
      visited[row, col] = 1
      if(row==data.shape[0]-1 and col==data.shape[1]-1):
        if(risk < found[-1]):
          logging.info(f'New Path found: {risk}')
          found.append(risk)
      elif(risk < found[-1]):
        self.down(risk, data, visited, row, col, found)
        self.up(risk, data, visited, row, col, found)
        self.left(risk, data, visited, row, col, found)
      visited[row, col] = 0
    col += 1
    return risk

  def down(self, risk, data, visited, row, col, found):
    row += 1
    if (row in range(data.shape[0]) and visited[row,col] == 0):
      risk += data[row, col]
      visited[row, col] = 1
      if(row==data.shape[0]-1 and col==data.shape[1]-1):
        if(risk < found[-1]):        
          logging.info(f'New Path found: {risk}')
          found.append(risk)
      elif(risk < found[-1]):  
        self.right(risk, data, visited, row, col, found)
        self.left(risk, data, visited, row, col, found)
        self.down(risk, data, visited, row, col, found)
      visited[row, col] = 0
    row -= 1
    return risk

  def up(self, risk, data, visited, row, col, found):
    row -= 1
    if (row in range(data.shape[0]) and visited[row,col] == 0):
      risk += data[row, col]
      visited[row, col] = 1
      if(row==data.shape[0]-1 and col==data.shape[1]-1):
        if(risk < found[-1]):
          logging.info(f'New Path found: {risk}')
          found.append(risk)
      elif(risk < found[-1]):
        self.right(risk, data, visited, row, col, found)
        self.left(risk, data, visited, row, col, found)
        self.up(risk, data, visited, row, col, found)
      visited[row, col] = 0
    row += 1
    return risk

  def part1(self, data):
    """Solve part 1"""
    riskScore = 0
    visited = np.zeros(data.shape)
    found = [1000]
    logging.debug(f'{data.shape}')
    data[0,0] = 0
    self.right(riskScore, data, visited, 0, -1, found)
    logging.debug(f'risk: {found}')
    return found[-1]

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

  sample = Day15()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()
