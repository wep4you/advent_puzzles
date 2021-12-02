import logging

class Day10:
  def __init__(self, inputfile):
    with open(inputfile, 'r') as f:
      for line in f:
        values = line.split()
        logging.debug(f'{values}')

  def part1(self):
      return ''

  def part2(self):
    return ''

def main():
  logging.basicConfig( level=logging.WARN)

  riddle = Day10('input.txt')

  answer1 = riddle.part1()
  answer2 = riddle.part2()

  print(f'Day 10-1: {answer1}')
  print(f'Day 10-2: {answer2}')

if __name__ == "__main__":
    main()