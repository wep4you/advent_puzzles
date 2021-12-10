# day.py

import logging
import pathlib
import sys

class Day10:
  
  puzzle_input = None
  puzzle_error_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
  }
  autocomplete_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
  }

  def __init__(self, inputFile=None):
    if (inputFile):
      logging.info(f"{inputFile}:")
      self.puzzle_input = pathlib.Path(inputFile).read_text().strip()
      logging.debug(f'Puzzle Input: {self.puzzle_input}')
    else:
      print(f'Please add Name of the inputfile to the call')
  
  def findCorrupted(self, input):
    logging.debug(f'{input}')
    stack = []
    for i, ch in enumerate(input):
      logging.debug(f'{i}: {ch}')
      if ch in ["(", "[", "{", "<"]:
        stack.append(ch)
        logging.debug(f'append: {stack}')
      else :
        if ch == ")":
          if stack[len(stack)-1] == "(":
            stack.pop()
            logging.debug(f'pop   : {stack}')
          else:
            logging.debug(f'Did not match: "{stack[len(stack)-1]}" <-> "{ch}"')
            return ch
        elif ch == "]":
          if stack[len(stack)-1] == "[":
            stack.pop()
            logging.debug(f'pop   : {stack}')
          else:
            logging.debug(f'Did not match: "{stack[len(stack)-1]}" <-> "{ch}"')
            return ch
        elif ch == "}":
          if stack[len(stack)-1] == "{":
            stack.pop()
            logging.debug(f'pop   : {stack}')
          else:
            logging.debug(f'Did not match: "{stack[len(stack)-1]}" <-> "{ch}"')
            return ch
        elif ch == ">":
          if stack[len(stack)-1] == "<":
            stack.pop()
            logging.debug(f'pop   : {stack}')
          else:
            logging.debug(f'Did not match: "{stack[len(stack)-1]}" <-> "{ch}"')
            return ch

    return [None, stack]

  def autoComplete(self, input):
    logging.debug(f'autocomplete: {input}')
    ret = []
    for i in range(len(input)-1, -1, -1):
      if input[i] == "(":
        ret.append(')')
      elif input[i] == "[":
        ret.append(']')
      elif input[i] == "{":
        ret.append('}')
      elif input[i] == "<":
        ret.append('>')
    return ret

  def calcAutoComplete(self, input):
    logging.debug(f'calcAutoComplete: {input}')
    ret = 0
    for val in input:
      ret = ret * 5 + self.autocomplete_scores[val]

    return ret

  def parse(self, puzzle_input):
    """Parse input"""
    return puzzle_input.split()

  def part1(self, data):
    """Solve part 1"""
    ret = 0
    for line in data:
      value = self.findCorrupted(line)[0]
      if(value in self.puzzle_error_scores):
        ret += self.puzzle_error_scores[value]

    return ret

  def part2(self, data):
    """Solve part 2"""
    scores = []
    for line in data:
      value = self.findCorrupted(line)
      if(value[0] == None):
        missing = self.autoComplete(value[1])
        calc = self.calcAutoComplete(missing)
        scores.append(calc)
        logging.debug(f'Incomplete: {value[1]} + {missing} ({calc})')

    scores.sort()
    middle = round((len(scores)-1)/2)
    middleScore = scores[middle]
    logging.debug(f'scores: {scores} - middle: {middleScore} ({middle}/{len(scores)})')

    return middleScore

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

  sample = Day10()

  for path in sys.argv[1:]:
    logging.info(f"{path}:")
    puzzle_input = pathlib.Path(path).read_text().strip()
    logging.debug(f'Puzzle Input: {puzzle_input}')
    solutions = sample.solve(puzzle_input)
    print("\n".join(str(solution) for solution in solutions))

if __name__ == "__main__":
    main()
