from math import prod

tree_map = """.......#................#......
...#.#.....#.##.....#..#.......
..#..#.#......#.#.#............
....#...#...##.....#..#.....#..
....#.......#.##......#...#..#.
...............#.#.#.....#..#..
...##...#...#..##.###...##.....
##..#.#...##.....#.#..........#
.#....#..#..#......#....#....#.
...........................#...
..........#.......#..#.....#.#.
..#.......###..#.#.......#.#...
....#..#....#....#..........#..
..##..#.......#.#...#..........
.....#.......#.....#....#......
..........##..#................
....##.#..###...#..##.....#.#..
..#..#.#.#...#......#...#.....#
....#.#....#...####.##.........
..#.........##...##.#..#..#....
.#......#...#..#..##.#.........
.#....#.......#..##..##..#.#.#.
...........#....#......#.......
..#....#....#...............#..
..#.....#....###.##.....#.#..#.
#..........#.#......#.#....#...
....###...#.#.....#....#.####.#
........#......#...#...#..##..#
...##..............##.#.......#
#..........#...........#.#....#
#...#....#..####..#............
###....#........#..............
...#.##....................#.##
...#..#.....#.....##...#....#..
.......###.#...#.........#.....
.#..#.....#.#..#.....#.........
#................#.............
...#......#.#.....##.#.#....#..
...#..#.#..#.....#...#....#....
.......#......#........#.....#.
.#.##..##.....#.#......#.#.#...
#...............#.....#....#...
.....#...........#..##.........
.....#..#........##..#..#.....#
..###.#.#.......#.#...........#
##....##....#.#....##...#.##.##
..................##.#.#.....#.
.#...........###...#...........
.#.#....#......#....###.#......
.......#.##...#...#..#.#.......
..#.....#.#....#..#............
.....#..#..#....#..#.........#.
..##.#......#.....#...#.#..#.#.
.........#......#....##.......#
#........#..#.#......#...#.#..#
...#....#.#..#....##.......###.
..#...#......#.##..........#...
........#..#..#...#.......#....
.##.#..#...#..#........#.#.####
#..#..#..........#....##...#...
....#...#........##........#...
.#......#.......#..#..#........
#...#.#......#....#............
#........#..##.#...##..........
...#..##.....#......##.#..#.#..
.#.#.....#.....#.####.#..##....
..........###....#.##...#......
.......#.......#..#.#.#.##.#..#
..#.#....#......#.#...#.......#
.#...#....#......#...#.........
.#....#..#....#.##.#....#..##..
...#..#.#..................#...
.##..#.............##.........#
...#.#.#................#.....#
...###..###..................#.
........##.##..#.#...#.....#...
.##...##...#...#....#...#......
#..#....#..#..#.#....#..####...
.#...............##....##.#....
#..#................#...#..#...
.#....#.....#..#.#........#....
...............##.#..##..##....
.#......#........#....#.#...#.#
.#.....#...##.#........#.##.#.#
..###............#..#.#....#...
..#.....#.........#....#..#.#..
.##.....#.#..........#.#....##.
...#...#....#..#......#.#.#..#.
#.....#...#....##...#.......##.
.......#.#.........##..........
............##.#.##...#.......#
.....#........##...#........#..
.#........#.#.#.#....#.........
#....#..#....#.#..#...#.#......
....##...........#...#...##.#.#
......#...##.###.....#.........
............#..##....##......#.
......##....#...#.#....#......#
#..#..#..#.#.#.........#...##.#
...#.........#...#.........##.#
#.#.....#.......#.##..#..#.....
##................#......#....#
....#..#.......#....##.....#...
.....#..#...#...#......#.#....#
..#....#.....#.........#.....#.
..#..#..........#.....#........
.......#..##.#......#.#........
.............##.....#....#.....
...#....#..#.#.#...............
........#....##..#...#........#
..##...............#.....#....#
........##.#.##.#......#..#....
..#.##.......#..........##..#..
.#..............#.#.##.........
.#.......#....#....#.#.#.......
.#.##.......#....#......###.#..
.......#...#............##.....
........#.#..........##..#.....
...###..#......#.....##..#..#..
...........##......#....#......
..............#....#..#..#.#..#
....#...#......#.##...#........
.#.............#..#......###.#.
#...#..#.#..............##..#.#
....................#.........#
..##..#......#.###.....#...#.#.
.#....#.#........#...#........#
..#....#.....#..............#..
##..........#..#..#...#........
...........#..##...#.......#...
........##.............#.......
#....#........#..#.#.###..#....
...........##..........##......
#......#.....##.#.##......##...
..#......#.........#.......#..#
......#.#....##..##.#...#.#...#
......#..................##....
...#....#.#...#.#.......##.....
#.#...##...##........#...##....
..#.......#.#.#...#............
.......#......#..#...#.........
#...#..#...........##..........
......#....#.........#.#....#..
#......#........#...#..##....#.
.....#.......##..#.#......#..#.
...........#......#...#......#.
#.#.##.....#....#.....##......#
.....##..#.#.#.###........#.#..
...#...#.#......#......#.......
......###....#..##...#.#.##....
#.....#.....#..................
...#...#......#...............#
..#............##..#.....#.....
.#....#...#...#...#...#..#.....
.##......#.........#.###.#.....
#.#.##.......##...#........##.#
.##.#.#......#.....#...#.....#.
....####.##.......#..##..##.#..
#.#.......#..##....###..#...#..
..#..#....#...#.#.#.#...#......
##.........#.##................
........#.....................#
..#...........#..#..##.#..#.#..
#...#...................#.###..
##..#............#.........#..#
...............##...#...##....#
#.#.....#..#.......#......#....
.#...#......#............#.....
#.......#...#..#....#.......#..
...#....#.##.#....#....#.#.....
...#..#..............#..#.#..#.
.........#.....#.#...#..#....#.
..#..#..#...##.....##.#.....#..
.#.#..........#........#.......
...............#........#.#.#..
.#......#.....#..............#.
........#.#..............#.#...
.......#.#....#..#.#.#..#.#.##.
...##..#...#.#..#...........#..
#...###.#.....#..#........#....
.#...##...##...##.#.....###....
.........#......#.#..##.#.#....
#....#.#..#...#.#.#....#..#..#.
.#.#...#......###.....#........
#.....#.#.......#..#.#...#.....
.................#.#....#..##..
#...........#....###..#......#.
##.#..#....#.#.#.#.............
#.....#..#...#........#........
..#..#......#..#.##.#..........
...#....#..#..........#.#.##.##
#........#...#.......#..##.#...
.#.#..#....#.#....#......#.....
##.......##.#........#...#..##.
##.##.....#.......#####.#....#.
..#..###.#.#..#....###..#.##..#
#.........#.............#.#...#
..#...##.#..................#..
.....#.#....#.#..#.#........#.#
......#.......#.#..##.#.#..#...
..#......#.#..##......#..#....#
..##..#..#.##.#..#....#...##...
###....#...##....##.........#..
#........##.........#......#..#
...#.........#......#.##.......
.....#.#.#....#......#.........
..#...........#....#......#.#..
##........#...##.....######....
....#..#..##.......#..#..#.....
..#....#..##....#......##....#.
...##....#........##......#....
.#.#...###...#......#..........
#....#..#.##.........#...#.....
......#..#.........#.##.....#..
...#............##....#......#.
...#.....##.....#........#.#..#
......#.#..#......#.....#..##..
#.#.........##..........#......
..###.....#..#....##..........#
.............##..#....#..##....
....#.#....##..#......#...#....
....###.....#..#.......#.......
............#..#...............
......#........#..#......#.....
.#........#.......#.##.......#.
..#.........#..#.#.....##....#.
...#.......#.......#.......##.#
#......##.#.....#......##.#..#.
#..........#.................#.
....#..##...........#.....#.#..
#.###...#............#.#....#.#
....#......#.#..###....##..#...
....#...#..........##..........
..#.#............#...#...###...
......#...#......#..#.#........
.#.......#..#...........##...#.
##...#...##....##.#..#..#.#....
.......#........#............##
.#......#...#.#................
#.#........#.#....#..#.##......
.......#.#...#....##.......##..
........#.#.#.........##..##...
..##...............#.#.###.#...
......#.#....#..#......##.....#
###.........#.....#.#.....##...
.#.#....#.....#.#.##..#.......#
..#..#.#......#...##..##.#..#..
...#........#..#....#..........
#...#.#...#..##....##..........
.........#........#.##....#..#.
..#...#.#.......##..........##.
###...........##.#......#.#..#.
...#....#...#..#..#......#.....
.....##.......###.#....###..##.
...#...#..........#.#......#...
....#.....##...##..#.#........#
.....#...#..#.....##...##....#.
................##.#.##....##.#
.#..#..#....#.....#....#..#...#
.....###.....#.................
#...#..##..#.........#.........
.....#..#................#.....
.#..#...#......#..#............
...#...#.#....#....##...#...##.
..........#....#.#..#.#.....#..
....#...###.##...#..#..#......#
#...#.......#..........#..#....
.#............#..##.......#...#
....#..#...#............#..#.#.
.#....#.......#..#.#......#....
...#...#............#...#.....#
....#.#.#..##.#.....#...#.#....
......#.#.#......#..#...#.....#
......##.....#.............#...
..#...#..#.#....#..............
.#.#..#....#.#..##....###.##...
..#...........#....#.###.#....#
.....#.........#.#.............
...#.#.....#......###......##..
...#...#.....#.................
...#..#...##.....##.........#..
..#...#..#..##..#...#........#.
##..#.#.##.#....#...........#..
.......#....##....#...##..#..#.
#.......##.#...##...##..#.....#
....#.#...............#......#.
....#.#...#.....#....#......#..
.#.........#.#....###........#.
.#.#.....#.....#.#.#....#.#....
............#...........#.#..##
#...#......#..#......#.#.......
...#.#.#.....#..#...#..##......
...#.#..#...#....#.........#.#.
........#..#......##.....#...#.
...#..#..............#..#......
.........#.......#...#......#..
.#......#.....#.....#......#...
......#.......#....#...#.#.....
.#.....#.##..#........#...#....
#.....##..##....#.#.......#..#.
.#..#...#..#.......#...........
..#..#...#.....##....#.....#...
#.#..............#....#..#.....
.........##...#......#.##...##.
.###...#.#...#.....#.........#.
.....#..........##...#..#....##
.#..#......#....##.#...#.......
.............###.#.#..#.#.#...#
.......#...##..#..#.....###....
##.......#...........#....#.#..
##......#...#.#................
.#.####..##.#...............#..
..#...#.#.#..#...#........#...#
.##..##.##.....#.......#..#.#..
...................#......#.#..
#.##..#..........#.............
##..#......#....#.#............
.#........#.....##...#.........
.##....#..#..##..........#...#.
#..........##........#..#..#.#.
####.###.#.....#....#..#.#....#
..#...#...#.#.......#....#...#.
......##.###..##.#.###......#.#"""

trees = {}
lines = tree_map.split("\n")
line_len = len(lines[0])
for translation in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    position = (0, 0)
    trees[translation] = 0
    while position[1] < len(lines):
        if lines[position[1]][position[0] % line_len] == "#":
            trees[translation] += 1
        position = (position[0]+translation[0], position[1]+translation[1])
print(prod(trees.values()))
