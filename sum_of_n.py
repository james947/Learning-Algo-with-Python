def sum1(n):
    # take an input of n and return the sum of the numbers from 0 to n
    final_sum=0
    for i in range(n+1):
        final_sum +=i
    print(final_sum)
sum1(1000)

# the second method solves with a formula hence it's faster
def sum2(n):
    # take an input of n and return the sum of the numbers from 0 to n
    return print((n*(n+1))/2)
sum2(1000)

# memory
# time

