#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
    elif length == 1:
        print([0])
    else:
        # Start the sequence with the first two numbers
        sequence = [0, 1]
        while len(sequence) < length:
            # Add the last two numbers to get the next one in the sequence
            next_fib = sequence[-1] + sequence[-2]
            sequence.append(next_fib)
        print(sequence)

# Example usage
print_fibonacci(9)

