def seq3np1(n):
    '''(int) -> int
    Print the 3n+1 sequence from n, terminating when it reaches 1.
    '''
    count = 0
    while n != 1:
        #print(n)
        count += 1
        if n % 2 == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    #print(n)                  # the last print is 1
    count += 1
    
    return count


i = 1
while seq3np1(i) != 12:
    i += 1

print(i, seq3np1(i))
