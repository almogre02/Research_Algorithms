import doctest
'''
Write an adjective named @lastcall. The capacitor(קשטן) checks whether the current input is the same as the input
the previous. If so - he writes an appropriate message. If not - it runs the function as usual.
'''

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
    >>> f2(-1) # Although the input is the same, the functions are different and should therefore return a value
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
    >>> f(f2(2))
    64
    >>> f2("a")
    I already told you that the answer is: aaaa
    >>> f(f2(2)) #f2(2) already exist ->therefore it returns a string
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for ** or pow(): 'NoneType' and 'int'
    >>> f2((1,2,3,4)) # returns an answer although the func got simillar input (but different type of structure)
    (1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4)
    """

    def wrapper(*args, **kwargs):
         # calls the @lastcall function
        if func.__name__ not in dict_ans: # the first time for this function
            value = func(*args, **kwargs)
            dict_ans[func.__name__]={}
            dict_ans[func.__name__][args]=value
            #print(value)
            return value
        elif func.__name__ in dict_ans and args not in dict_ans[func.__name__]: # more than 1 time but with a different value
            value = func(*args, **kwargs)
            dict_ans[func.__name__][args]=value
            #print(value)
            return value
        else:
            print(f'I already told you that the answer is: {dict_ans[func.__name__][args]}')

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


@lastcall
def f3(x: int):
    return x * 2


if __name__ == '__main__':
    print(f(2)) # expect: 4
    print(f(3))  # expect: 9
    print(f(4))  # expect: 16
    print(f1(f2(1))) # expect: 64
    print(f(f1(f2(5))))  # expect: 64000000
    print(f(2))  # expect: I already told you that the answer is: 2
    print(f1(4))  # expect: I already told you that the answer is: 64 (row number 83)
    '''   Different DataStructures with the same value   '''
    l = [1,2,3]
    t= (1,2,3)
    #print(f3(l)) # expect: [1, 2, 3, 1, 2, 3]
    print(f3(t)) # expect: (1, 2, 3, 1, 2, 3)
    #print(f3(l)) # expect: I already told you that the answer is: [1, 2, 3, 1, 2, 3]
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))

