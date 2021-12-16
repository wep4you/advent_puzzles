# Day 15: Chiton

## Part 1

### Source

https://adventofcode.com/2021/day/15

### Question

What is the lowest total risk of any path from the top left to the bottom right?

### Answer

Check Python script: [day15.py](./day15.py)

---

## Part 2

### Source

https://adventofcode.com/2021/day/15#part2

### Question

Using the full map, what is the lowest total risk of any path from the top left to the bottom right?


### Answer

Check Python script: [day15.py](./day15.py)

---

## Notes

First attemt with just recursively check all possible ways, just works on examplet input, even with
the first input set, to slow to get to an end. Has to be solved with a algorythm, so had a look at
the solutions and used an example with the **Dijkstra's** algorythm. Some nice explanation could be found here: [Understanding Dijkstra's Algorithm](http://blog.aos.sh/2018/02/24/understanding-dijkstras-algorithm/)