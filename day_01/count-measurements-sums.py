lines_as_int = []

with open('input.txt', 'r') as f:
  for line in f:
    numbers = line.split()
    for number in numbers:
        try:
            lines_as_int.append(int(number))
        except:
            print ('can not cast to integer')

last_measurement_sum = -1
increased = 0
decreased = 0
nochange = 0

for i in range(len(lines_as_int)-2):
    measurement_sum = lines_as_int[i] + lines_as_int[i+1] + lines_as_int[i+2]
 
    if last_measurement_sum > -1:
        if (last_measurement_sum > measurement_sum):
            print(f'{i}: {lines_as_int[i]} + {lines_as_int[i+1]} + {lines_as_int[i+2]} = {measurement_sum} (decreased)')
            decreased += 1
        elif (last_measurement_sum ^ measurement_sum):
            print(f'{i}: {lines_as_int[i]} + {lines_as_int[i+1]} + {lines_as_int[i+2]} = {measurement_sum} (increased)')
            increased += 1
        else:
            print(f'{i}: {lines_as_int[i]} + {lines_as_int[i+1]} + {lines_as_int[i+2]} = {measurement_sum} (no change)')
            nochange += 1
    else:
        print(f'{i}: {lines_as_int[i]} + {lines_as_int[i+1]} + {lines_as_int[i+2]} = {measurement_sum} - (N/A - no previous measurement)')
    
    last_measurement_sum = measurement_sum

print(f'increased: {increased} - decreased: {decreased} - nochange {nochange}')