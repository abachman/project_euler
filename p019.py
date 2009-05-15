"""
2008-01-24

You are given the following information, but you may prefer to do some 
research for yourself. 

    * 1 Jan 1900 was a Monday. (BUT THE PROBLEM STARTS IN 1901)
    * Thirty days has September,
      April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    * A leap year occurs on any year evenly divisible by 4, but 
      not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth 
century (1 Jan 1901 to 31 Dec 2000)? 
"""

mdays = [31,28,31,30,31,30,31,31,30,31,30,31]
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

def is_leap(year):
    if year % 4 == 0 and (not year % 100 == 0) or year % 400 == 0:
        return True
    return False

def weekday():
    while 1:
        yield 0 # Tuesday (Jan 1, 1901) 
        yield 1
        yield 2
        yield 3
        yield 4
        yield 5
        yield 6 # Monday

named = ['m','t','w','r','f','s','sun']
wday = weekday()
count = 0
curday = 0

for y in range(1901,2001):
##    print 'year',y
    m = 0
    for month in mdays:
        day = wday.next()
        if day == 5:
            print '1-%s-%i' % (months[m], y)
            count += 1
           
        if month == 28 and is_leap(y):
            month = 29
        for d in range(month - 1):
            day = wday.next()

        m += 1
print count, curday
            

