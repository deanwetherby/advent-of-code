# day 21

Step counter. Similar to previous days where we recurse on the positions.

## part 1

goal is to count how many plots could be reached within 64 steps

First thought that this was the number (sum) of total plots that could be reached.

Ends up being the number of plots at the end of the 64 steps.

## part 2

infinite map is exactly the provided example from part1

One way to enable the infinite map is to allow traversing the small map by looping to the other side. A move down from the bottom row ends up at the top row for example.

Then we are looking for cycles in order to jump ahead.
