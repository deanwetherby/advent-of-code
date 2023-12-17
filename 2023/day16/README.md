# day 16

This was the first day I attempted to use a board state over string manipulation.

I noticed that other day's solutions used complex numbers for the board so I wanted to try it.

## part 1

While relatively straight-forward to create the board state, I had to pair the position with the velocity for the beam state. This was a mental hurdle that I was happy to finally overcome.

```python
board = {complex(i,j): col for j, row in enumerate(data)
         for i, col in enumerate(row.strip())}
```

I used a deque to stack the beams as I iterated. If any valid splitters were encountered while traversing the grid, I added them to the stack. The initial beam was run all the way through; until the beam exited the grid or a previous beam registration was encounter (both position and velocity).

The first attempt at storing the energized state did not work as I was not accounting for the direction in which the beam entered the grid cell. The energized state was a copy of the board state dictionary using the position as the dictionary key. While it did keep track if the cell was energized, it did not provide a good exit condition for the beam. Once I realized that the grid cell could be entered from one of four direction, I made the change to using a set.

Another mistake I made was in the calculation of the energized cells. I used the length of the list comprehension over positions to determine the number of cells that had been energized and was surprised to learn that the number was too high. It took me forever to figure out that ignoring the direction component meant that I could have the same position in the list four times which was why the length was higher than expected. I converted the list to a set to get the unique positions which yielded the correct answer. The minus one is for the inital beam state which is off-grid.

```python
#WRONG
print(len([x for x, _ in energized])-1)

# RIGHT
print(len(set([x for x, _ in energized]))-1)
```

## part 2

I leveraged part 1 and turned the beam traversing logic into a fucntion. I called the function with the initial beam position in part 1 and got the same answer so I was on the right track.

```python
def energize(initial: tuple[complex, complex]) -> int:
    beams = deque([initial])
    energized = set()
    while beams:
        pos, vel = beams.popleft()
        while not (pos, vel) in energized:
            energized.add((pos, vel))
            pos += vel
            cell = board.get(pos)
            if cell == "|":
                vel = 1j
                beams.append((pos,-vel))
            elif cell == "-":
                vel = -1
                beams.append((pos,-vel))
            elif cell == "/":
                vel = -complex(vel.imag, vel.real)
            elif cell == "\\":
                vel = complex(vel.imag, vel.real)
            elif cell is None:
                break
    return len(set(x for x,_ in energized))-1
```

I decided to make a list of all starting positions just outside the grid pointing in. It took me quite a while to wrap my head around the real and imaginary start positions.

I made these constants to deal with directions which seems easy enough. The real component moves left/right and the imaginary moves up/down.

```python
DOWN = complex(0, 1)
UP = complex(0, -1)
RIGHT = complex(1, 0)
LEFT = complex(-1, 0)
```

Once I had the list of start positions, I just ran each of them and maximized on the resultant energy scores.

```python
print(max(map(energize, start_beams)))
```
