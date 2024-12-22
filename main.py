from math import log2, ceil
def counting_attempts(num):
    return ceil(log2(num + 1))

guessed_number = int(input())
counting_attempts(guessed_number)