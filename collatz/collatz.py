#!usr/bin/python3

def collatz(n=1):
    """
    Run a collatz conjecture on a given integer
    Returns number of steps to get to 1 (Does not include starting number
    as a step)
    """
    if type(n) is not int or n < 1:
        return False
    steps = 0
    while (n != 1):
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
        steps += 1
    return steps
