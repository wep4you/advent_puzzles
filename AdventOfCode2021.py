import logging

from day_01 import day01
from day_02 import day02
from day_03 import day03

def main():
  logging.basicConfig(level=logging.WARN)
  
  riddle_01 = day01.Day01('./day_01/input.txt')
  print(f'Day 01-1: {riddle_01.part1()}')
  print(f'Day 01-2: {riddle_01.part2()}')

  riddle_02 = day02.Day02('./day_02/input.txt')
  print(f'Day 02-1: {riddle_02.part1()}')
  print(f'Day 02-2: {riddle_02.part2()}')

  riddle_03 = day03.Day03('./day_03/input.txt')
  print(f'Day 03-1: {riddle_03.part1()}')
  print(f'Day 03-2: {riddle_03.part2()}')


if __name__ == "__main__":
    main()



