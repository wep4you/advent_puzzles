import logging

from day_01 import day01
from day_02 import day02
from day_03 import day03
from day_04 import day04
from day_05 import day05
from day_06 import day06
from day_07 import day07
from day_08 import day08
from day_09 import day09
from day_10 import day10
from day_11 import day11
from day_12 import day12
from day_13 import day13
from day_14 import day14
from day_15 import day15
from day_16 import day16
from day_17 import day17
from day_18 import day18
from day_19 import day19
from day_20 import day20
from day_21 import day21
from day_22 import day22
from day_23 import day23
from day_24 import day24

def main():
  logging.basicConfig(level=logging.WARN)
  
  riddle = day01.Day01('./day_01/input.txt')
  print(f'Day 01-1: {riddle.part1()}')
  print(f'Day 01-2: {riddle.part2()}')

  riddle = day02.Day02('./day_02/input.txt')
  print(f'Day 02-1: {riddle.part1()}')
  print(f'Day 02-2: {riddle.part2()}')

  riddle = day03.Day03('./day_03/input.txt')
  print(f'Day 03-1: {riddle.part1()}')
  print(f'Day 03-2: {riddle.part2()}')

  riddle = day04.Day04('./day_04/input.txt')
  print(f'Day 04-1: {riddle.part1()}')
  print(f'Day 04-2: {riddle.part2()}')

  riddle = day05.Day05('./day_05/input.txt')
  print(f'Day 05-1: {riddle.part1()}')
  print(f'Day 05-2: {riddle.part2()}')

  riddle = day06.Day06('./day_06/input.txt')
  answer = riddle.solve()
  print(f'Day 06-1: {answer[0]}')
  print(f'Day 06-2: {answer[1]}')

  riddle = day07.Day07('./day_07/input.txt')
  answer = riddle.solve()
  print(f'Day 07-1: {answer[0]}')
  print(f'Day 07-2: {answer[1]}')

  riddle = day08.Day08('./day_08/input.txt')
  answer = riddle.solve()
  print(f'Day 08-1: {answer[0]}')
  print(f'Day 08-2: {answer[1]}')

  riddle = day09.Day09('./day_09/input.txt')
  answer = riddle.solve()
  print(f'Day 09-1: {answer[0]}')
  print(f'Day 09-2: {answer[1]}')

  riddle = day10.Day10('./day_10/input.txt')
  answer = riddle.solve()
  print(f'Day 10-1: {answer[0]}')
  print(f'Day 10-2: {answer[1]}')

  riddle = day11.Day11('./day_11/input.txt')
  answer = riddle.solve()
  print(f'Day 11-1: {answer[0]}')
  print(f'Day 11-2: {answer[1]}')

  riddle = day12.Day12('./day_12/input.txt')
  answer = riddle.solve()
  print(f'Day 12-1: {answer[0]}')
  print(f'Day 12-2: {answer[1]}')

  riddle = day13.Day13('./day_13/input.txt')
  answer = riddle.solve()
  print(f'Day 13-1: {answer[0]}')
  print(f'Day 13-2: {answer[1]}')

  riddle = day14.Day14('./day_14/input.txt')
  answer = riddle.solve()
  print(f'Day 14-1: {answer[0]}')
  print(f'Day 14-2: {answer[1]}')

  riddle = day15.Day15('./day_15/input.txt')
  answer = riddle.solve()
  print(f'Day 15-1: {answer[0]}')
  print(f'Day 15-2: {answer[1]}')

  riddle = day16.Day16('./day_16/input.txt')
  answer = riddle.solve()
  print(f'Day 16-1: {answer[0]}')
  print(f'Day 16-2: {answer[1]}')

  riddle = day17.Day17('./day_17/input.txt')
  answer = riddle.solve()
  print(f'Day 17-1: {answer[0]}')
  print(f'Day 17-2: {answer[1]}')

  riddle = day18.Day18('./day_18/input.txt')
  answer = riddle.solve()
  print(f'Day 18-1: {answer[0]}')
  print(f'Day 18-2: {answer[1]}')

  riddle = day19.Day19('./day_19/input.txt')
  answer = riddle.solve()
  print(f'Day 19-1: {answer[0]}')
  print(f'Day 19-2: {answer[1]}')

  riddle = day20.Day20('./day_20/input.txt')
  answer = riddle.solve()
  print(f'Day 20-1: {answer[0]}')
  print(f'Day 20-2: {answer[1]}')

  riddle = day21.Day21('./day_21/input.txt')
  answer = riddle.solve()
  print(f'Day 21-1: {answer[0]}')
  print(f'Day 21-2: {answer[1]}')

  riddle = day22.Day22('./day_22/input.txt')
  answer = riddle.solve()
  print(f'Day 22-1: {answer[0]}')
  print(f'Day 22-2: {answer[1]}')

  riddle = day23.Day23('./day_23/input.txt')
  answer = riddle.solve()  
  print(f'Day 23-1: {answer[0]}')
  print(f'Day 23-2: {answer[1]}')

  riddle = day24.Day24('./day_24/input.txt')
  answer = riddle.solve()
  print(f'Day 24-1: {answer[0]}')
  print(f'Day 24-2: {answer[1]}')

if __name__ == "__main__":
    main()

