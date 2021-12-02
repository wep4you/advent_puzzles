lines_as_int = []

with open('input.txt', 'r') as f:
  for line in f:
    numbers = line.split()
    for number in numbers:
        try:
            lines_as_int.append(int(number))
        except:
            print ('can not cast to integer')

i=0
last_measurement = -1
increased = 0
decreased = 0
nochange = 0

for measurement in lines_as_int:
    i += 1
    if last_measurement > -1:
        if (last_measurement > measurement):
            print(f'{i}: {last_measurement} > {measurement} (decreased)')
            decreased += 1
        elif (last_measurement < measurement):
            print(f'{i}: {last_measurement} < {measurement} (increased)')
            increased += 1
        else:
            print(f'{i}: {last_measurement} == {measurement} (no change)')
    else:
        print(f'{i}: {last_measurement} - {measurement} - (N/A - no previous measurement)')
        
    last_measurement = measurement

print(f'increased: {increased} - decreased: {decreased} - nochange {nochange}')