import doctest

dict_ans = {}
def lastcall(func):
    """
    >>> f(5)
    25
    >>> f1(-1)
    -1
    >>> f2(100)
    400
    >>> f(6)
    36
    >>> f1(6) # Although the input is the same, the functions are different and should therefore return a value
    216
    >>> f(5)
    I already told you that the answer is: 25
    >>> f2(-1)
    -4
    >>> f2(0)
    0
    >>> f2(299978)
    1199912
    >>> f2(100)
    I already told you that the answer is: 400
    >>> f("Invalid input") # can't do str**2
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'
    >>> f(0)
    0
    >>> f1(0) # Although the input is the same, the functions are different and should therefore return a value
    0
    >>> f2("a")
    'aaaa'
    >>> f2([1,2,3,4])
    [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
    >>> f(f2(2))
    64
    >>> f2("a")
    I already told you that the answer is: aaaa
    >>> f(f2(2))
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
    """

    def wrapper(*args, **kwargs):
        value = func(*args, **kwargs)
        if func.__name__ not in dict_ans:
            dict_ans[func.__name__]=[]
            dict_ans[func.__name__].append(value)
            #print(value)
            return value
        elif func.__name__ in dict_ans and value not in dict_ans[func.__name__]:
            dict_ans[func.__name__].append(value)
            #print(value)
            return value
        else:
            print(f'I already told you that the answer is: {value}')

    return wrapper



@lastcall
def f(x: int):
    return x ** 2


@lastcall
def f1(x: int):
    return x ** 3


@lastcall
def f2(x: int):
    return x * 4


if __name__ == '__main__':
    print(f(2)) # expect: 4
    print(f(3))  # expect: 9
    print(f(4))  # expect: 16
    print(f1(f2(1))) # expect: 16
    print(f(f1(f2(5))))  # expect: 343
    print(f(2))  # expect: I already told you that the answer is: 2
    print(f1(4))  # expect: I already told you that the answer is: 64 (row number 85)
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

