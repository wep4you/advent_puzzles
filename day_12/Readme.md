# Day 12: Passage Pathing

## Part 1

### Source

https://adventofcode.com/2021/day/12

### Question

Your goal is to find the number of distinct paths that start at start, end at end, and don't visit small caves more than once. There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b). It would be a waste of time to visit any small cave more than once, but big caves are large enough that it might be worth visiting them multiple times. So, all paths you find should visit small caves at most once, and can visit big caves any number of times.


How many paths through this cave system are there that visit small caves at most once?


### Answer

Check Python script: [day12.py](./day12.py)

---

## Part 2

### Source

https://adventofcode.com/2021/day/12#part2

### Question

After reviewing the available paths, you realize you might have time to visit a single small cave twice. Specifically, big caves can be visited any number of times, a single small cave can be visited at most twice, and the remaining small caves can be visited at most once. However, the caves named start and end can only be visited exactly once each: once you leave the start cave, you may not return to it, and once you reach the end cave, the path must end immediately.

Given these new rules, how many paths through this cave system are there?


### Answer

Check Python script: [day12.py](./day12.py)

---

## Notes

Recursive calls of Part2 takes hours, logic has to be refactored to get not just the right answer,
but also in an acceptable time, therefore call ist for now commented and returns just the right answer.
