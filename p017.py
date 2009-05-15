"""
2007-12-20

If the numbers 1 to 5 are written out in words: one, two, three, 
four, five; there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were 
written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred 
and forty-two) contains 23 letters and 115 (one hundred and fifteen)
contains 20 letters.
"""

nums = {0:'', 1:'one', 2:'two', 3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',
        9:'nine',
        10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',
        16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',
        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',60:'sixty',70:'seventy',
        80:'eighty',90:'ninety'}

def splode(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n = n / 10
    return l

def num_to_word(n):
    nplaces = splode(n)
    if len(nplaces) > 1:
        if nplaces[1] == 1:
            nplaces[1] = nplaces[0] + 10 
            nplaces[0] = 0
        else:
            nplaces[1] = nplaces[1] * 10
    s = ''
    nplaces = [i for i in reversed(nplaces)]
    if n > 999:
        s += nums[ nplaces[0] ]
        s += 'thousand'
        nplaces.pop(0)
    if n > 99:
        s += nums[ nplaces[0] ] 
        if nplaces[0] > 0:
            s += 'hundred'
        if n % 100 != 0:
            s+= 'and'
        nplaces.pop(0)
    if n > 9:
        s+= nums[ nplaces[0] ]
        nplaces.pop(0)
    s += nums[ nplaces[0] ]
    return s


assert len(num_to_word(342)) == 23
assert len(num_to_word(115)) == 20

#for n in xrange(1000, 1243):
#    print num_to_word(n)

li = []
for n in xrange(1, 1001):
    li.append(num_to_word(n))
print sum(map(len, li))
# 21124
