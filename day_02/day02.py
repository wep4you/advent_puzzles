import logging

class Course:
  def __init__(self, direction, distance):
    self.direction = direction
    self.distance = distance

class Day02:
  CourseInput = []

  def __init__(self, inputfile):
    with open(inputfile, 'r') as f:
      for line in f:
        direction = line.split()
        point = Course(direction[0], int(direction[1]))
        self.CourseInput.append(point)

  def part1(self):
      depth = 0
      horizontal = 0

      for i in range(len(self.CourseInput)):
          dist = self.CourseInput[i].distance
          dir = self.CourseInput[i].direction
          logging.debug(f'{i}: {dir} {dist}')
          if (dir == "up"):
              horizontal -= dist
          elif (dir == "down"):
              horizontal += dist
          elif (dir == "forward"):
              depth += dist
          else:
            logging.warn(f'{i}: Unknown direction {dir}')

      logging.info(f'Horizontal: {horizontal} - Depth: {depth} - Course: {horizontal * depth}')
      return horizontal * depth

  def part2(self):
    depth = 0
    horizontal = 0
    aim = 0

    for i in range(len(self.CourseInput)):
      dist = self.CourseInput[i].distance
      dir = self.CourseInput[i].direction
      logging.debug(f'{i}: {dir} {dist}')
      if (dir == "down"):
        aim += dist
      elif (dir == "up"):
        aim -= dist
      elif (dir == "forward"):
        horizontal += dist
        depth += aim * dist
      else:
        logging.warn(f'{i}: Unknown direction {dir}')

    logging.info(f'Horizontal: {horizontal} - Depth: {depth} - course: {horizontal * depth}')
    return horizontal * depth

def main():
  logging.basicConfig( level=logging.WARN)

  riddle = Day02('input.txt')

  answer1 = riddle.part1()
  answer2 = riddle.part2()

  print(f'Answer Day 02 Part 1: {answer1}')
  print(f'Answer Day 02 Part 2: {answer2}')

if __name__ == "__main__":
    main()