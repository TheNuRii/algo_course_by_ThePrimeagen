from typing import List
from math import floor

def binary_search(arr: List, searched_number) -> bool:
    l = 0
    r = len(arr)

    while l < r:
        m = floor(l + (r - l)/2)
        v = arr[m]
    
        if searched_number > v:
            l = m + 1
        else:
            r = m

    if searched_number == l:
        return True
    else:
        return False

arr = []
for i in range(1000):
    arr.append(i)

print(binary_search(arr, 999))