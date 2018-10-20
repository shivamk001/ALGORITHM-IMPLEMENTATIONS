#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
      l=len(a)
      s=0
      for i in range(0, l):
            for j in range(0, l-1):
                  if(a[j] > a[j+1]):
                        t=a[j]
                        a[j]=a[j+1]
                        a[j+1]=t
                        s+=1
      print("Array is sorted in", s, "steps")
      print("Array after sort: ", a)
      
if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))
    print("Array before sort: ", a)
    countSwaps(a)
