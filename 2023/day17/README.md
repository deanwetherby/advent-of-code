# day 17 - path planning

Dijkstra's or A* seem like the obvious choice.

## part 1

Committed to using the complex board grid from day 16 to build on that capability.

First time implementing A* from scratch in python using the complex board.

Had significant challenges with the following error:

`TypeError: '<' not supported between instances of 'complex' and 'complex'`

This occurred when using either PriorityQueue or heapq.
