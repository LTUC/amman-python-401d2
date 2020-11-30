""" Iteration
    n           5 4  3  2    1
    output      5 20 60 120  return
"""
def fact_using_loops(n):
    if n == 0 or n == 1:
        return 1
    output = 1
    while (n>1):
        output = output * n
        n -= 1
    return output


""" Recursion
    fact(5) = 5 * fact(4)
                4 * fact(3)
                    3 * fact(2)
                        2 * fact(1)
                            1
"""
def fact(n):
    # Special case
    if n == 0:
        return 1
    # Base case
    if n == 1:
        return 1
    # Recursive call
    return n * fact(n-1)
