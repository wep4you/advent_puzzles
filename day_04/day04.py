import logging

class BingoCard:
  def __init__(self, cardNumber):
    self.cardNumber = cardNumber
    self.values = []
    self.hits = []

  def addRow(self, row):
    self.values.append(row)
    hitinit = []
    for i in range(len(row)):
      hitinit.append(0)
    self.hits.append(hitinit)
    logging.debug(f'Row added {self.cardNumber}: {self.values}')

  def drawn(self, drawnNumber):
    for a in range(len(self.values)):
      for b in range(len(self.values[a])):
        if self.values[a][b] == drawnNumber:
          self.hits[a][b] = 1


  def checkBingo(self):
    bingo = self.bingo_horizontal()
    if bingo == False:
      bingo = self.bingo_vertical()
    return bingo

  def bingo_horizontal(self):
    bingo = False
    for a in range(len(self.hits)):
      row = True
      for b in range(len(self.hits[a])):
        if self.hits[a][b] == 0:
          row = False
          break
      if row:
        bingo = True
        logging.info(f'BINGO (horizontal) - Card: {self.cardNumber} - Row: {a}')
        break
    return bingo

  def bingo_vertical(self):
    bingo = False
    for a in range(len(self.hits[0])):
      col = True
      for b in range(len(self.hits)):
        if self.hits[b][a] == 0:
          col = False
          break
      if col:
        bingo = True
        logging.info(f'BINGO (vertical) - Card: {self.cardNumber} - Col: {a}')
        break
    return bingo

  def sumUmarked(self):
    sum = 0
    for a in range(len(self.hits)):
      for b in range(len(self.hits[a])):
        if self.hits[a][b] == 0:
          sum += int(self.values[a][b])
    return sum

  def printCard(self):
    print(f'Card: {self.cardNumber}')
    for row in self.values:
      print(f'{row}')

  def printHits(self):
    print(f'Card: {self.cardNumber}')
    for row in self.hits:
      print(f'{row}')

class Day04:
  winningNumers = []
  bingoCards = []

  def __init__(self, inputfile):
    with open(inputfile, 'r') as f:
      i = 0
      cardNumber = -1

      for line in f:
        values = line.split()
        if (i > 0):
          logging.debug(f'{i}: bingovalues: {values}')
          if (len(values) == 0):
            cardNumber += 1
            self.bingoCards.append(BingoCard(cardNumber))
            logging.debug(f'New card: {cardNumber} - input line: {i}')
          else:
            self.bingoCards[cardNumber].addRow(values)
        else:
          self.winningNumers = values[0].split(',')
          logging.info(f'winning numbers {i}: {values}')
        i += 1

      if (logging.getLogger().level == logging.DEBUG):
        for i in range(len(self.bingoCards)):
          self.bingoCards[i].card.printCard()
          self.bingoCards[i].printHits()


  def part1(self):
    answer = 0
    i = 1
    for drawn in self.winningNumers:
      logging.info(f'{i}: Drawn number: {drawn}')

      bingo = False
      for card in self.bingoCards:
        card.drawn(drawn)
        bingo = card.checkBingo()
        if bingo:
          if (logging.getLogger().level == logging.INFO):
            card.printCard()
            card.printHits()

          sum = card.sumUmarked()
          answer = int(drawn) * sum
          logging.info(f'winning number: {drawn} - sum not checked: {sum}')
          break
      if bingo:
        break

      i += 1

    return answer


  def part2(self):
    answer = 0
    i = 1
    winningCards = []
    lastDrawn = 0
 
    for drawn in self.winningNumers:
      logging.info(f'{i}: Drawn number: {drawn}')

      bingo = False
      for card in self.bingoCards:
        if card.cardNumber not in winningCards:
          card.drawn(drawn)
          bingo = card.checkBingo()
          if bingo:
            if card.cardNumber not in winningCards:
              winningCards.append(card.cardNumber)
              lastDrawn = int(drawn)
      i += 1

    logging.info(f'winningCards {len(winningCards)} - {winningCards} - lastwin: {winningCards[len(winningCards)-1]}')
    
    lastBingo = self.bingoCards[winningCards[len(winningCards)-1]]

    if lastBingo:
      if (logging.getLogger().level == logging.INFO):
        lastBingo.printCard()
        lastBingo.printHits()

      sum = lastBingo.sumUmarked()
      answer = int(lastDrawn) * sum
      logging.info(f'last winning number: {lastDrawn} - sum not checked: {sum}')

    return answer

def main():
  logging.basicConfig( level=logging.INFO)

  riddle = Day04('input.txt')

  answer1 = riddle.part1()
  answer2 = riddle.part2()

  print(f'Day 04-1: {answer1}')
  print(f'Day 04-2: {answer2}')

if __name__ == "__main__":
    main()