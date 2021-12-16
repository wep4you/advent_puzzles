# Day 14: Extended Polymerization

## Part 1

### Source

https://adventofcode.com/2021/day/14

### Question

Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?



### Answer

Check Python script: [day14.py](./day14.py)

---

## Part 2

### Source

https://adventofcode.com/2021/day/14#part2

### Question

Apply 40 steps of pair insertion to the polymer template and find the most and least common elements in the result. What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?

### Answer

Check Python script: [day14.py](./day14.py)

---

## Notes

Simple Solution as for Part1 was not possible becaue of eather Memory and time limitation, optimizations with
recursive calls and counter, worked for small input and got rid of the memory limitation but also not possible
within from performance for more iterations than around 28, so problem has to be solved with other logic.
Had no idea, therefore I have to had a look on other solution, it was likely the laternfish puzzle so at the
end a simple and fast solution, also learned alot about new modules in itertools (pairwise was exactly what was needed),
and also from collections and lambda functions.