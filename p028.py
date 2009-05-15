"""
Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

      21 22 23 24 25 
      20  7  8  9 10
      19  6  1  2 11
      18  5  4  3 12
      17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in
the same way?
"""

import psyco; psyco.full()

# Step lists
square = 1001
UR = [n * 8 for n in range(1, int(square / 2) + (square%2!=0 and 1 or 0))] #[8, 16, 24, ...]
DR = [n - 6 for n in UR] #[2, 10, 18, ...]
DL = [n - 4 for n in UR] #[4, 12, 20, ...]
UL = [n - 2 for n in UR] #[6, 14, 22, ...]

_sum = 1
for LIST in (UR, DR, DL, UL):
  s = 1
  for n in LIST:
    s += n
    _sum += s
print _sum

