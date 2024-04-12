import math
import os
import random
import re
import sys

def countSwaps(a):
    swaps = 0
    
    def bubble_sort(a):
        nonlocal swaps
        n = len(a)
        for i in range(n):
            for j in range(n - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swaps += 1

    bubble_sort(a)
    print("Array is sorted in", swaps, "swaps.")
    print("First Element:", a[0])
    print("Last Element:", a[-1])

if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)
