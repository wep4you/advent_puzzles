# Day 6: Lanternfish

## Part 1

### Source

https://adventofcode.com/2021/day/6

### Question

Find a way to simulate lanternfish. How many lanternfish would there be after 80 days?s

### Answer

Check Python script: [day06.py](./day06.py)

---

## Part 2

### Source

https://adventofcode.com/2021/day/6#part2

### Question

How many lanternfish would there be after 256 days?

### Answer

Check Python script: [day06.py](./day06.py)

---

## Notes

Nice example to optimize code execution from Part-1 to Part-2. Started in part one with simple arrays,
this is ok, for some smaller iterations, but gets worse with higher iterations and high memory usage.
So refactored code in Part-2 to dictionary and also changed code for Part-1.

Added Unit Test to easy check examples and practise TDD with pytest