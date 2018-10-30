
import random
import timeit

"""
    Priscilla Short
    Compare recursive binary search to looping binary search using randon ints
    
    Description of problem:
    Use the binary search functions given in the text (recursive and iterative).
    Generate a random, ordered list of integers and do a benchmark analysis for each one.
    What are your results? Can you explain them?
    
    Answer:
    the slice operator in Python, used in the recursive version is actually O(k).
    This means that the binary search using slice will not perform in strict logarithmic time, which makes it slower in its current state.
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

def recurBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint]==item:
            return True
        else:
            if item<alist[midpoint]:
                return binarySearch(alist[:midpoint],item)
            else:
                return binarySearch(alist[midpoint+1:],item)



print("        Recurse          While Loop")
recur = timeit.Timer("recurBinarySearch(lst, searchFor)", "from __main__ import recurBinarySearch, lst, searchFor")
whileL = timeit.Timer("binarySearch(lst, searchFor)", "from __main__ import binarySearch, lst, searchFor")
for i in range(100000,2000001,100000):
    lst = [random.randint(1,i+1) for item in range(i)]
    searchFor = random.randint(1,i+1)
    timeRecurse = recur.timeit(number=1)
    timeWhile = whileL.timeit(number=1)
    print("%15.5f, %15.5f" %(timeRecurse,timeWhile))


