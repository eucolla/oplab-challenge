# Game of Stones

"""
import math, import os, import random, import re, import sys

# Complete the gameOfStones function below.
def gameOfStones(n):

    if __name__ == '__main__':
        fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)

        fptr.write(result + '\n')

    fptr.close()
"""

num = int(input("Enter the number of moves: "))
for i in range(0, num):
    if int(input("Enter the amount of stones: ")) % 7 > 1:
        print("First")
    else:
        print("Second")
