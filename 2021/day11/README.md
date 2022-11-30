# Day 11: Dumbo Octopus

You enter a large cavern full of rare bioluminescent dumbo octopuses!
They seem to not like the Christmas lights on your submarine, so you turn them off for now.

There are 100 octopuses arranged neatly in a 10 by 10 grid.
Each octopus slowly gains energy over time and flashes brightly for a moment when its energy is full.
Although your lights are off, maybe you could navigate through the cave without disturbing the octopuses if you could predict when the flashes of light will happen.

Each octopus has an energy level - your submarine can remotely measure the energy level of each octopus (your puzzle input).
For example:
```
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
```
The energy level of each octopus is a value between 0 and 9.
Here, the top-left octopus has an energy level of 5, the bottom-right one has an energy level of 6, and so on.

You can model the energy levels and flashes of light in steps.
During a single step, the following occurs:

First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes.
This increases the energy level of all adjacent octopuses by 1, including octopuses that are diagonally adjacent.
If this causes an octopus to have an energy level greater than 9, it also flashes.
This process continues as long as new octopuses keep having their energy level increased beyond 9.
(An octopus can only flash at most once per step.)
Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.
Adjacent flashes can cause an octopus to flash on a step even if it begins that step with very little energy.
Consider the middle octopus with 1 energy in this situation:

Before any steps:
```
11111
19991
19191
19991
11111
```
After step 1:
```
34543
40004
50005
40004
34543
```
After step 2:
```
45654
51115
61116
51115
45654
```

Here is how the larger example above progresses:

Before any steps:
```
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
```
After step 1:
```
6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637
```
After step 2:
```
8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848
```

After step 3:
```
0050900866
8500800575
9900000039
9700000041
9935080063
7712300000
7911250009
2211130000
0421125000
0021119000
```

After step 10:
```
0481112976
0031112009
0041112504
0081111406
0099111306
0093511233
0442361130
5532252350
0532250600
0032240000
```

After step 10, there have been a total of 204 flashes.
Fast forwarding, here is the same configuration every 10 steps:

After step 20:
```
3936556452
5686556806
4496555690
4448655580
4456865570
5680086577
7000009896
0000000344
6000000364
4600009543
```

After step 30:
```
0643334118
4253334611
3374333458
2225333337
2229333338
2276733333
2754574565
5544458511
9444447111
7944446119
```

After step 40:
```
6211111981
0421111119
0042111115
0003111115
0003111116
0065611111
0532351111
3322234597
2222222976
2222222762
```

After 100 steps, there have been a total of 1656 flashes.

Given the starting energy levels of the dumbo octopuses in your cavern, simulate 100 steps.
**How many total flashes are there after 100 steps?**
