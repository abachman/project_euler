"""
2007-12-20
By starting at the top of the triangle below and moving to adjacent 
numbers on the row below, the maximum total from top to bottom is 23. 

3
7 5
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click 
and 'Save Link/Target As...'), a 15K text file containing a triangle 
with one-hundred rows. 

NOTE: This is a much more difficult version of Problem 18. It is not 
possible to try every route to solve this problem, as there are 299 
altogether! If you could check one trillion (10^12) routes every second 
it would take over twenty billion years to check them all. There is an 
efficient algorithm to solve it. ;o) 
"""
import psyco
psyco.full()

nums = [r for r in file('triangle.txt')]
nums = [map(int, n.split()) for n in nums]

def maxr(row, prevrow):
    li = []
    for n in range(len(row)):
        try:
            li.append( max(row[n] + prevrow[n], row[n] + prevrow[n+1]) )
        except:
            print n, row, prevrow
            raise
    return li

def solve(nums):
    nums.append([0] * (len(nums)+1))
    #print nums
    nrow = maxr(nums[-2], nums[-1])
    #print nrow
    for r in range(len(nums)-3, -1, -1): 
        #print r, nums[r], nrow
        nrow = maxr(nums[r], nrow)
    return nrow[0]
    
if __name__=="__main__":
    # from random import randint
    # li = []
    # for x in range(100):
        # li.append([])
    # for x in range(1,101):
        # for i in range(x):
            # li[x-1].append(randint(1,99))
    # print li[:20]
    # print solve(li)
    print solve(nums)
# 1070
