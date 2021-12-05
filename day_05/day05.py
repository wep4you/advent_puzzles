import logging

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Line:
  def __init__(self, x1, y1, x2, y2):
    self.start = Point(x1, y1)
    self.end = Point(x2, y2)

  def getCoordinates(self, diagonals):
    coordinates = []
    logging.info(f'getCoordinates() x:({self.start.x},{self.end.x}) - y:({self.start.y}, {self.end.y}))')

    stepX = 1
    if (self.start.x > self.end.x):
      stepX = -1
    minX = self.start.x
    maxX = self.end.x + stepX

    stepY = 1
    if (self.start.y > self.end.y):
      stepY = -1
    minY = self.start.y
    maxY = self.end.y + stepY

    if (self.start.y == self.end.y):
      y = self.start.y
      for x in range(minX, maxX, stepX):
        coordinates.append(Point(x, y))
    elif (self.start.x == self.end.x):
      x = self.start.x
      for y in range(minY, maxY, stepY):
        coordinates.append(Point(x, y))
    elif (diagonals):
      x = minX
      y = minY
      while x != maxX and y != maxY:
        coordinates.append(Point(x, y))
        x += stepX
        y += stepY

    return coordinates

  def printStartEnd(self):
    print(f'startX: {self.start.x}, startY: {self.start.y} -> endX: {self.end.x}, endY: {self.end.y}')

  def printCoordinates(self, diagonals):
    for point in self.getCoordinates(diagonals):
      print(f'{point.x}, {point.y}')

class Day05:
  input = []
  xMax = None
  yMax = None

  def __init__(self, inputfile, xMax=1000, yMax=1000):
    self.xMax=xMax
    self.yMax=yMax
    with open(inputfile, 'r') as f:
      for line in f:
        values = line.split()
        logging.debug(f'{values}')
        start = values[0].split(',')
        end = values[2].split(',')
        line = Line(int(start[0]), int(start[1]), int(end[0]), int(end[1]))    
        self.input.append(line)

  def initArea(self, area):
    for y in range(self.yMax):
      area.append([])
      for x in range(self.xMax):
        area[y].append(0)

  def drawLine(self, area, line, diagonals):
    points = line.getCoordinates(diagonals)

    for point in points:
      logging.debug(f'drawLine Point: ({point.x},{point.y}) - area ({len(area)}, {len(area[0])})')
      area[point.x][point.y] += 1

  def printArea(self, area):
    for y in range(self.yMax):
      line = ''
      for x in range(self.xMax):
        if (area[x][y] == 0):
          line += '.'
        else:
          line += str(area[x][y])
      print(f'{line}')

  def countDensityPointsMin(self, area):
    count = 0
    for x in range(self.xMax):
      for y in range(self.yMax):
        if (area[x][y] >= 2):
          count += 1
    return count

  def part1(self):
    area = []

    self.initArea(area)
    if (logging.getLogger().level == logging.DEBUG):
      self.printArea(area)

    logging.info(f'DrawArea: 0,{len(area)} -> 0,{len(area[0])}')

    for line in self.input:
      if (logging.getLogger().level == logging.DEBUG):
        line.printStartEnd()
        line.printCoordinates(False)
      self.drawLine(area, line, False)

    if (logging.getLogger().level == logging.INFO):
      self.printArea(area)

    points = self.countDensityPointsMin(area)

    return points

  def part2(self):
    area = []

    self.initArea(area)
    if (logging.getLogger().level == logging.DEBUG):
      self.printArea(area)

    logging.info(f'DrawArea: 0,{len(area)} -> 0,{len(area[0])}')

    for line in self.input:
      if (logging.getLogger().level == logging.DEBUG):
        line.printStartEnd()
        line.printCoordinates(True)
      self.drawLine(area, line, True)

    if (logging.getLogger().level == logging.INFO):
      self.printArea(area)

    points = self.countDensityPointsMin(area)

    return points


def main(DEV=False):

  if (DEV):
    logging.basicConfig( level=logging.DEBUG)
    sample = Day05('example.txt', 10, 10)

    sample1 = sample.part1()
    sample2 = sample.part2()

    logging.debug(f'EXAMPLE Day 05-1: {sample1}')
    logging.debug(f'EXAMPLE Day 05-1: {sample2}')

  else:
    logging.basicConfig( level=logging.WARN)
    riddle = Day05('input.txt', 1000, 1000)

    answer1 = riddle.part1()
    answer2 = riddle.part2()

    print(f'Day 05-1: {answer1}')
    print(f'Day 05-2: {answer2}')

if __name__ == "__main__":
    main(False)