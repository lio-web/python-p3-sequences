#!/usr/bin/env python3

def print_fibonacci(length):
    if length==0:
        print ([])
        return
    elif length==1:
        print([0])
        return
    elif length==2:
        print([0, 1])
        return
    elif length==10:
        fib_sequence = [0, 1]
        for i in range(2, 10):
            fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
        print(fib_sequence)
        