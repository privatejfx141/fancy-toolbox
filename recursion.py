def factorial(n):
    '''(int) -> int
    '''
    return n if (n == 1) else (n * factorial(n-1))


def fibonacci(n):
    '''(int) -> int
    '''
    return n if (n <= 1) else (fibonacci(n-1) + fibonacci(n-2))


def fib(n):
    '''(int) -> int
    '''
    return fibonacci(n)


def triangular_num(n):
    '''(int) -> int
    '''
    return n if (n == 1) else (n + triangular_num(n-1))


def gcd(m, n):
    '''(int, int) -> int
    '''
    return n if (m % n == 0) else gcd(n, m % n)


def sum_r_list(r_list):
    '''(list of numbers) -> int

    Return the sum of all the numbers in r_list.

    >>> r_list = [1, 2, 3, 4, 5, 6, 7, [1, 2, 3, [], 3, 1], 32, [3, [0], 4, 3]]
    >>> sum_r_list(r_list)
    80
    '''
    total_sum = 0
    for element in r_list:
        c_type = type(element)
        if c_type == int or c_type == float:
            total_sum += element
        elif c_type == list:
            total_sum += sum_r_list(element)

    return total_sum


def exists_r_list(r_list, target):
    '''(list, item) -> bool

    Return True iff target is in r_list.

    >>> exists_r_list([1, [2, 3], 4, [5, [6 , [], [8, 9]], 10]], 8)
    True
    '''

    exists = False
    count = 0
    while count < len(r_list) and not exists:
        element = r_list[count]
        if element == target:
            exists = True
        elif isinstance(element, list):
            exists = exists_r_list(element, target)
        count += 1

    return exists


if __name__ == '__main__':
    import doctest
    single_line = [i for i in range(10)]
    print(single_line)
