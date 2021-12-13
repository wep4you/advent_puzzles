# day.py

import enum
import logging
import pathlib
import sys
import re

import numpy as np

class Day13:
  
  puzzle_input = None

  def __init__(self, inputFile=None):
    if (inputFile):
      logging.info(f"{inputFile}:")
      self.puzzle_input = pathlib.Path(inputFile).read_text().strip()
      logging.debug(f'Puzzle Input: {self.puzzle_input}')
    else:
      logging.debug(f'Please add Name of the inputfile to the call')
  
  def parse(self, puzzle_input):
    """Parse input"""
    input_parts = puzzle_input.split('\n\n')
    logging.debug(f'{input_parts}')
    coord = []
    inCoord = input_parts[0].split()
    for values in inCoord:
      value = values.split(',')
      coord.append([int(value[0]), int(value[1])])

    fold = []
    for values in input_parts[1].split('\n'):
      value = re.split(' |=', values)
      fold.append([value[2], int(value[3])])

    npCoord = np.array(coord)
    npFold = np.array(fold)
    logging.debug(f'{npCoord} - ({npCoord.shape})')
    logging.debug(f'{npFold} - ({npFold.shape})')

    return npCoord, npFold

  def initArray(self, data):
    npCoord = data[0]
    npFold =  data[1]

    xSize = 0
    ySize = 0
    if (npFold[0, 0] == 'x'):
      ySize = int(npFold[0, 1]) * 2 + 1
      xSize = int(npFold[1, 1]) * 2 + 1
    elif (npFold[0, 0] == 'y'):
      xSize = int(npFold[0, 1]) * 2 + 1
      ySize = int(npFold[1, 1]) * 2 + 1

    mat = np.zeros((xSize, ySize), dtype=np.int64)
    mat[npCoord[:,1], npCoord[:,0]] = 1
    logging.debug(f'{mat} - ({mat.shape})')

    return mat

  def foldHorizontal(self, data, pos):
    upper = data[:pos,:]
    logging.debug(f'upper:\n{upper}')
    lower = data[pos+1:,:]
    logging.debug(f'lower:\n{lower}')
    lowerFlip = np.flipud(lower)
    logging.debug(f'lowerFlipped:\n{lowerFlip}')

    ret = upper + lowerFlip
    np.putmask(ret, ret > 1, 1)
    logging.debug(f'added:\n{ret}')

    return ret

  def foldVertical(self, data, pos):
    left = data[:,:pos]
    logging.debug(f'left:\n{left}')
    right = data[:,pos+1:]
    logging.debug(f'right:\n{right}')
    rightFlip = np.fliplr(right)
    logging.debug(f'rightFlip:\n{rightFlip}')

    ret = left + rightFlip
    np.putmask(ret, ret > 1, 1)
    logging.debug(f'added:\n{ret}')

    return ret

  def part1(self, data, flips=1):
    """Solve part 1"""
    npFold =  data[1]
    mat = self.initArray(data)
    logging.debug(f'{mat} - ({mat.shape})')
    
    for i, folding in enumerate(npFold):
      direction = folding[0]
      pos = int(folding[1])
      logging.debug(f'{i}: fold: {direction} - {pos}')
      if (direction == 'x'):
        mat = self.foldVertical(mat, pos)
      elif (direction == 'y'):
        mat = self.foldHorizontal(mat, pos)

      if(i >= flips-1):
        break

    return mat.sum()


  def part2(self, data):
    """Solve part 2"""
    npFold =  data[1]
    mat = self.initArray(data)
    logging.debug(f'{mat} - ({mat.shape})')
    
    for folding in npFold:
      direction = folding[0]
      pos = int(folding[1])
      logging.debug(f'fold: {direction} - {pos}')
      if (direction == 'x'):
        mat = self.foldVertical(mat, pos)
      elif (direction == 'y'):
        mat = self.foldHorizontal(mat, pos)


    xShapeOri = mat.shape
    mat.resize((1,xShapeOri[0]*xShapeOri[1]))
    index = np.where(mat==1)
    logging.debug(f'{index}')
    xArray = np.full((1, xShapeOri[0]*xShapeOri[1]), ' ')
    xArray[index] = '#'
    logging.debug(f'{xArray} - ({xArray.shape})')
    xArray = xArray.reshape((xShapeOri))
    logging.debug(f'{xArray} - ({xArray.shape})')

    ret = ""
    for line in xArray:
      ret += ("".join(line)) + "\n"

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

  sample = Day13()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()
