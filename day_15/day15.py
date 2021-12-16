# day.py

import logging
import pathlib
import sys
from typing import Tuple
import numpy as np
from queue import PriorityQueue, Queue
from point2d import Point2D

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


  def dijkstra(self, weights: dict[Point2D, int], start: Point2D, end: Point2D) -> int:
    visited: set[Point2D] = set()
    lowest_weights: dict[Point2D, int] = {}

    queue: Queue[Tuple[int, Point2D]] = PriorityQueue()
    queue.put((0, start))
    while not queue.empty():
      # position with lowest weight from the start so far
      weight_from_start, pos = queue.get()
      logging.debug(f'pos lowest: {weight_from_start}, {pos}')
      if pos == end:
        # party time
        logging.debug(f'!!!! party time !!!!')
        return weight_from_start

      # update neighbor weights
      x, y = pos
      for neighbor in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if neighbor not in weights or neighbor in visited:
          # been there, done that
          logging.debug(f'been there, done that {neighbor}')
          continue

        new_weight = weight_from_start + weights[neighbor]
        old_weight = lowest_weights.get(neighbor)
        if old_weight and new_weight >= old_weight:
          # you can do better than that
          logging.debug(f'you can do better than that old: {old_weight} < new: {new_weight}')
          continue

        # found a more efficient route: update weight and add to queue
        logging.debug(f'found a more efficient route: {neighbor} {new_weight}')
        lowest_weights[neighbor] = new_weight
        queue.put((new_weight, neighbor))

      visited.add(pos)


  def part1(self, data):
    weights: dict[Point2D, int] = {}
    for y, line in enumerate(data):
      for x, weight in enumerate(line):
        weights[(int(x), int(y))] = int(weight)
    logging.debug(f'weights: {weights}')

    start=(0, 0)
    end=(data.shape[0]-1, data.shape[1]-1)
    logging.debug(f'start: {start} - end {end}')

    ret = self.dijkstra(weights, start, end)
    logging.debug(f'solution: {ret}')

    return ret

  def initField(self, data):
    newData = data.copy()
    for _ in range(4):
      newData = newData.copy()
      newData += 1
      newData[newData == 10] = 1
      data = np.hstack((data, newData))
    logging.debug(f'{data}')
    newData = data.copy()
    for _ in range(4):
      newData = newData.copy()
      newData += 1
      newData[newData == 10] = 1
      data = np.vstack((data, newData))
    logging.debug(f'{data}')
    return data


  def part2(self, data):
    """Solve part 2"""
    input = self.initField(data)
    return self.part1(input)


  def solve(self, puzzle_input=None):
    """Solve the puzzle for the given input"""
    if (puzzle_input is None):
      puzzle_input = self.puzzle_input
    data = self.parse(puzzle_input)
    logging.debug(data)
    solution1 = self.part1(data)
    solution2 = self.part2(data)

    return solution1, solution2


  """
  Recursion didnt work -> efiizient slgorythm needed
  Just for documentation
  START
  """
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
        #self.up(risk, data, visited, row, col, found)
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
        #self.up(risk, data, visited, row, col, found)
        #self.left(risk, data, visited, row, col, found)
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
        #self.left(risk, data, visited, row, col, found)
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
        #self.left(risk, data, visited, row, col, found)
        #self.up(risk, data, visited, row, col, found)
      visited[row, col] = 0
    row += 1
    return risk

  def part1_recursive(self, data):
    """Solve part 1"""
    riskScore = 0
    visited = np.zeros(data.shape)
    found = [1000]
    logging.debug(f'{data.shape}')
    data[0,0] = 0
    self.right(riskScore, data, visited, 0, -1, found)
    logging.debug(f'risk: {found}')
    return found[-1]
  """
  END
  """

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
