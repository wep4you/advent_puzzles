import logging

class Day06:

  inputFishAges = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}

  def __init__(self, inputfile):
    with open(inputfile, 'r') as f:
      for line in f:
        values = line.split()[0].split(',')
        for value in values:
          self.inputFishAges[int(value)] += 1
        logging.debug(self.inputFishAges)

  def part1(self, dayCount=80):
    fishAges = self.inputFishAges
    for i in range (dayCount):
      tmpfishAges = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
      for key in fishAges:
        if (key == 0):
          tmpfishAges[8] += fishAges[key]
          tmpfishAges[6] += fishAges[key]
        else:
          tmpfishAges[key-1] += fishAges[key]
      fishAges = tmpfishAges
      logging.debug(f'Day {i+1}: {fishAges}')
    logging.info(f'Day {i+1}: {fishAges}')

    fishCount = 0
    for key in fishAges:
      fishCount += fishAges[key]

    return fishCount


  def part2(self, dayCount=256):
    return self.part1(dayCount)


def main(DEV=False):
  if (DEV):
    logging.basicConfig( level=logging.DEBUG)
    sample = Day06('example.txt')

    logging.info(f'EXAMPLE Day 06-1:  18 days: {sample.part1(18)}')
    logging.info(f'EXAMPLE Day 06-1:  80 days: {sample.part1(80)}')
    logging.info(f'EXAMPLE Day 06-2: 256 days: {sample.part2(256)}')

  else:  
    logging.basicConfig( level=logging.WARN)

    riddle = Day06('input.txt')

    answer1 = riddle.part1(80)
    answer2 = riddle.part2(256)

    print(f'Day 06-1: {answer1}')
    print(f'Day 06-2: {answer2}')

if __name__ == "__main__":
    main(False)