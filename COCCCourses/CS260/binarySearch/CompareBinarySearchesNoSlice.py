
import random
import timeit

"""
    Priscilla Short
    Compare recursive binary search without slice to looping binary search using randon ints
    
    Description of problem:
    Implement the binary search using recursion without the slice operator.
    Recall that you will need to pass the list along with the starting and
    ending index values for the sublist. Generate a random, ordered list of
    integers and do a benchmark analysis.
"""

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False
	
    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

def recurBinarySearch(alist, item, start, end):
    if start == end: #len(alist) == 0:
        return False
    else:
        midpoint = ((end - start)//2) + start
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return recurBinarySearch(alist, item, start, midpoint)
            else:
                return recurBinarySearch(alist, item, midpoint+1, end)


print("        Recurse          While Loop")
recur = timeit.Timer("recurBinarySearch(lst, searchFor, 0, len(lst))", "from __main__ import recurBinarySearch, lst, searchFor")
whileL = timeit.Timer("binarySearch(lst, searchFor)", "from __main__ import binarySearch, lst, searchFor")
for i in range(100000,2000001,100000):
    lst = [item for item in range(i)]
    searchFor = random.randint(1,i+1)
    timeRecurse = recur.timeit(number=1)
    timeWhile = whileL.timeit(number=1)
    print("%15.5f, %15.5f" %(timeRecurse,timeWhile))


