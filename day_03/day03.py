import logging


class Day03:
  diagnostic_data = []

  def __init__(self, inputfile):
    with open(inputfile, 'r') as f:
      for line in f:
        values = list(line.rstrip())
        logging.debug(f'{values}')
        self.diagnostic_data.append(values)

  def part1(self):
    counter = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(self.diagnostic_data)):
      for x in range(len(self.diagnostic_data[i])):
        logging.debug(f'{self.diagnostic_data[i][x]}')
        if (self.diagnostic_data[i][x] == '0'):
          counter[x] -= 1
        elif (self.diagnostic_data[i][x] == '1'):
          counter[x] += 1
        else:
          logging.warn(f'Wrong Format')

    logging.debug(f'counter: {counter}')

    gamma_bin = ''
    epsilon_bin = ''
    for y in range(len(counter)):
      if (counter[y] > 0):
        gamma_bin += '1'
        epsilon_bin += '0'
      else:
        gamma_bin += '0'
        epsilon_bin += '1'

    gamma = int(gamma_bin, 2)
    epsilon = int(epsilon_bin, 2)

    logging.info(f'gamma: {gamma} ({gamma_bin}) - epsilon: {epsilon} ({epsilon_bin})')

    return gamma * epsilon


  def selectOxygen(self, pos, array):

    counter = 0
    for i in range(len(array)):
      if (array[i][pos] == '0'):
        counter -= 1
      elif (array[i][pos] == '1'):
        counter += 1
      else:
        logging.warn(f'Wrong Format')

    new_array = []
    for i in range(len(array)):

      if (counter >= 0):
        if (array[i][pos] == '1'):
          new_array.append(array[i])
      else:
        if (array[i][pos] == '0'):
          new_array.append(array[i])

    if (len(new_array) == 0):
      new_array = array

    if (logging.getLogger().level == logging.DEBUG):
      logging.debug(f'{pos}: counter: {counter} - arraycount: {len(new_array)}')
      for i in range(len(new_array)):
        logging.debug(f'new_array: {new_array[i]}')

    return new_array



  def selectCO2(self, pos, array):
    counter = 0
    for i in range(len(array)):
      if (array[i][pos] == '0'):
        counter -= 1
      elif (array[i][pos] == '1'):
        counter += 1
      else:
        logging.warn(f'Wrong Format')

    new_array = []
    for i in range(len(array)):

      if (counter >= 0):
        if (array[i][pos] == '0'):
          new_array.append(array[i])
      else:
        if (array[i][pos] == '1'):
          new_array.append(array[i])

    if (len(new_array) == 0):
      new_array = array

    if (logging.getLogger().level == logging.DEBUG):
      logging.debug(f'{pos}: counter: {counter} - arraycount: {len(new_array)}')
      for i in range(len(new_array)):
        logging.debug(f'new_array: {new_array[i]}')

    return new_array


  def part2(self):
    oxygen_data = self.diagnostic_data
    for x in range(len(self.diagnostic_data[0])):
      oxygen_data = self.selectOxygen(x, oxygen_data)
    logging.debug(f'Oxygen: {oxygen_data}')

    co2_data = self.diagnostic_data
    for x in range(len(self.diagnostic_data[0])):
      co2_data = self.selectCO2(x, co2_data)
    logging.debug(f'CO2: {co2_data}')
 
    oxygen_bin = ''
    for y in range(len(oxygen_data[0])):
      oxygen_bin += oxygen_data[0][y]
    oxygen = int(oxygen_bin, 2)

    co2_bin = ''
    for y in range(len(co2_data[0])):
      co2_bin += co2_data[0][y]
    co2 = int(co2_bin, 2)

    logging.info(f'oxygen: {oxygen} ({oxygen_bin}) - co2: {co2} ({co2_bin})')

    return oxygen * co2



def main():
  logging.basicConfig( level=logging.INFO)

  riddle = Day03('input.txt')

  answer1 = riddle.part1()
  answer2 = riddle.part2()

  print(f'Day 03-1: {answer1}')
  print(f'Day 03-2: {answer2}')

if __name__ == "__main__":
    main()