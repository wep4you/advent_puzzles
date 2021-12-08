import logging
import pathlib
import sys
import numpy as np

class Day08:
  
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
    lines = puzzle_input.split('\n')
    for line in lines:
      part = line.split('|')
      tmpIn = []
      for value in part[0].split():
        tmpIn.append(value)
      logging.debug(f'tmpIn: {tmpIn}')
      tmpOut = []
      for value in part[1].split():
        tmpOut.append(value)
      logging.debug(f'tmpOut: {tmpOut}')
      ret.append([tmpIn, tmpOut])
    logging.info(f'ret: {ret}')
    return ret

  def analyzeInput(self, input):
    code = {}
    complex = False
    for value in input:
      logging.debug(f'analyze: {value}')
      valLen = len(value)
      if (valLen == 2):
        code[1] = value
        logging.debug(f'1 == {value}')
      elif(valLen == 4):
        code[4] = value
        logging.debug(f'4 == {value}')
      elif(valLen == 3):
        code[7] = value
        logging.debug(f'7 == {value}')
      elif(valLen == 7):
        code[8] = value
        logging.debug(f'8 == {value}')
      else:
        logging.debug(f'to check: {value}')
        complex = True
    
    if(complex):
      code = self.analyzeComplexInput(input, code)

    return code

  def countSimilarities(self, value, code, digit):
    compCount = 0
    if (digit in code):
      for i in code[digit]:
        logging.debug(f'digit: {i}')
        if (value.find(i) != -1):
          compCount += 1
      logging.debug(f'{digit} - compCount: {compCount}')
    return compCount

  def analyzeComplexInput(self, input, code):
    for value in input:
      logging.debug(f'analyze: {value}')
      valLen = len(value)
      if (valLen == 5 and not (2 in code and 3 in code and 5 in code)):
        logging.info(f'{value} - could be 2, 3, 5 ({code})')
        compWith1 = self.countSimilarities(value, code, 1)
        logging.debug(f'compWith1: {compWith1}')
        if (compWith1 == 2):
          if (not 3 in code):
            code[3] = value
            logging.debug(f'3 == {value}')
        else:
          compWith4 = self.countSimilarities(value, code, 4)
          logging.debug(f'compWith4: {compWith4}')
          if (compWith4 == 2):
            if (not 2 in code):
              code[2] = value
              logging.debug(f'2 == {value}')            
          elif (compWith4 == 3):
            if (not 5 in code):
              code[5] = value
              logging.debug(f'5 == {value}')

      elif (valLen == 6 and not (0 in code and 6 in code and 9 in code)):
        logging.info(f'{value} - could be 0, 6, 9 ({code})')
        compWith4 = self.countSimilarities(value, code, 4)
        logging.debug(f'compWith4: {compWith4}')
        if (compWith4 == 4):
          if (not 9 in code):
            code[9] = value
            logging.debug(f'9 == {value}')
        elif (compWith4 == 3):
          compWith1 = self.countSimilarities(value, code, 1)
          logging.debug(f'compWith1: {compWith1}')
          if (compWith1 == 2):
            if (not 0 in code):
              code[0] = value
              logging.debug(f'0 == {value}')
          elif (compWith1 == 1):
            if (not 6 in code):
              code[6] = value
              logging.debug(f'6 == {value}')
    return code

  def calculateOut(self, output, code):
    logging.debug(f'calc: {output} - ({code})')
    sumTxt = ''
    for value in output:
      for i in range (10):
        sim = self.countSimilarities(value, code, i)
        if(len(value) == len(code[i]) and sim == len(value)):
          logging.debug(f'found --{i}-- compare: {value}({len(value)}) == {code[i]}({sim})')
          sumTxt += str(i)
          break
    return int(sumTxt)

  def part1(self, data):
    """Solve part 1"""
    sumUniqeDigits = 0
    for input in data:
      for out in input[1]:
        valLen = len(out)
        logging.debug(f'{out} - {valLen}')
        if (valLen == 2 or valLen == 3 or valLen == 4 or valLen == 7 ):
          sumUniqeDigits += 1

    return sumUniqeDigits

  def part2(self, data):
    """Solve part 2"""
    output = 0
    for values in data:
      code = self.analyzeInput(values[0])
      lineSum = self.calculateOut(values[1], code)
      logging.debug(f'SUM: {lineSum} - ({values[1]})')
      output += lineSum

    return output

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

  sample = Day08()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()
