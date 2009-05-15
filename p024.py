'''
A permutation is an ordered arrangement of objects. For example, 3124
is one possible permutation of the digits 1, 2, 3 and 4. If all of the
permutations are listed numerically or alphabetically, we call it
lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2,
3, 4, 5, 6, 7, 8 and 9?
'''

def permutations(li):
  """ Return all permutations of a given list.  This funtion assumes
  every element of the list is unique. """
  if len(li) <= 1:
    yield li
  else:
    for el in li:
      for p in permutations([e for e in li if not e == el]):
        yield [el] + p

def solve():
  count = 1
  p = permutations('0123456789')
  while count < 1000000:
    p.next()
    count+=1
  print strf(p.next())

def strf(li):
  """stringify a list of objects.
  protects against 'TypeError: expected string, int found' """
  return ''.join(map(str, li))

if __name__=="__main__":
  from time import time
  s = time()
  solve() # 2783915460
  print time() - s 
  #for p in permutations(('1',1,'0',0)):
  #  print p

  
  
