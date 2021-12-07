# Day 7: The Treachery of Whales

## Part 1

### Source

https://adventofcode.com/2021/day/7

### Question

Determine the horizontal position that the crabs can align to using the least fuel possible. How much fuel must they spend to align to that position?


### Answer

Check Python script: [day07.py](./day07.py)

---

## Part 2

### Source

https://adventofcode.com/2021/day/7#part2

### Question

Determine the horizontal position that the crabs can align to using the least fuel possible so they can make you an escape route! How much fuel must they spend to align to that position?

### Answer

Check Python script: [day07.py](./day07.py)

---

## Notes

With Unit Tests and check Test Cases against the examples, it's much easier to focus on solution. 

Tried different Solutions for performance optimization on Part 2, with code samples within the
Unit tests on the Real Data input and output of the processing time, to print the output start wit -s

## Performance Outcomes

Best performance with the right calculation and reduction of loops
Get the outcomes in the Unit Tests with

    pytest -s

### Just with Loops and math

19,55 sec: Easiest but slowest variant

### Use Numpy

10,74 sec: Better Performace sort input array, remove duplicates, use min and max from Numpy

### Calculiaton

00,11 sec: Best Performance, no need for nested loops, just calculate the fuel needs

### Calculiaton and Numpy

00,35 sec: Overhead for sorting and stripping duplicates are higher than the removed inner loop, so not so performanct
