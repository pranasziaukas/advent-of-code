# Advent of Code 2021

[![test](https://github.com/pranasziaukas/advent-of-code-2021/actions/workflows/test.yml/badge.svg)](https://github.com/pranasziaukas/advent-of-code-2021/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/pranasziaukas/advent-of-code-2021/blob/main/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## What is it?

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels.
It can be solved in any programming language you like.
People use them as a speed contest, interview prep, company training, university coursework, practice problems, etc.

## How to use it?

[Here](https://adventofcode.com/2021) is the 2021 version.

Then do `make solution day=<number>` to create a solution folder based on the (very) simple template and have fun!

## Part Two

Next, you need to find the largest basins so you know what areas are most important to avoid.

A basin is all locations that eventually flow downward to a single low point.
Therefore, every low point has a basin, although some basins are very small.
Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point.
```
The example above has four basins:
The top-left basin, size 3
The top-right basin, size 9
The middle basin, size 14
The bottom-right basin, size 9
```
Find the three largest basins and multiply their sizes together. In the above example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?