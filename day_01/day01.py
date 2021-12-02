import logging

class Day01:
  lines_as_int = []
  def __init__(self, inputfile):
    with open(inputfile, 'r') as f:
      for line in f:
        numbers = line.split()
        for number in numbers:
          try:
            self.lines_as_int.append(int(number))
          except:
            logging.error('can not cast to integer')

  def part1(self):
      last_measurement = -1
      increased = 0
      decreased = 0
      nochange = 0

      for i in range(len(self.lines_as_int)):
        measurement = self.lines_as_int[i]
        if last_measurement > -1:
          if (last_measurement > measurement):
            logging.debug(f'{i}: {last_measurement} > {measurement} (decreased)')
            decreased += 1
          elif (last_measurement < measurement):
            logging.debug(f'{i}: {last_measurement} < {measurement} (increased)')
            increased += 1
          else:
            logging.debug(f'{i}: {last_measurement} == {measurement} (no change)')
        else:
          logging.debug(f'{i}: {last_measurement} - {measurement} - (N/A - no previous measurement)')
            
        last_measurement = measurement

      logging.info(f'increased: {increased} - decreased: {decreased} - nochange {nochange}')
      return increased


  def part2(self):
    last_measurement_sum = -1
    increased = 0
    decreased = 0
    nochange = 0

    for i in range(len(self.lines_as_int)-2):
      measure0 = self.lines_as_int[i]
      measure1 = self.lines_as_int[i+1]
      measure2 = self.lines_as_int[i+2]

      measurement_sum = measure0 + measure1 + measure2
  
      if last_measurement_sum > -1:
        if (last_measurement_sum > measurement_sum):
          logging.debug(f'{i}: {measure0} + {measure1} + {measure2} = {measurement_sum} (decreased)')
          decreased += 1
        elif (last_measurement_sum ^ measurement_sum):
          logging.debug(f'{i}: {measure0} + {measure1} + {measure2} = {measurement_sum} (increased)')
          increased += 1
        else:
          logging.debug(f'{i}: {measure0} + {measure1} + {measure2} = {measurement_sum} (no change)')
          nochange += 1
      else:
        logging.debug(f'{i}: {measure0} + {measure1} + {measure2} = {measurement_sum} - (N/A - no previous measurement)')
      
      last_measurement_sum = measurement_sum

    logging.info(f'increased: {increased} - decreased: {decreased} - nochange {nochange}')
    return increased


def main():
  logging.basicConfig(level=logging.WARN)
  
  riddle = Day01('input.txt')

  answer1 = riddle.part1()
  answer2 = riddle.part2()

  print(f'Answer Day 01 Part 1: {answer1}')
  print(f'Answer Day 01 Part 2: {answer2}')

if __name__ == "__main__":
    main()
