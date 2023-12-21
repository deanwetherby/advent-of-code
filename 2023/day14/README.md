# Day 14

## Part 1

Part 1 seemed easy.
Rotate the board
String split on #
Sort the section so that O "rolls" north
Recombine the sections using "#".join()
Sum the O indices to the score

## Part 2

Gross. Cycle NWSE 1 BILLION times. That's 4 BILLION rotations!
Wrapped part 1 in a loop of 1 Billion 4-part rotations.
Might take 6 years to finish.
I'd like to cache the rotations but the list of strings is not hashable.
Tuples are however.

First time doing cycles.
