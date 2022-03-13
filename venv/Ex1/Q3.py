import doctest
import inspect

"""
Newton's method:  find_root -> this function gets a function and two real numbers,
and finds its root in the defined domain by the numbers. 
Got help from GeeksforGeeks to derivative function.
"""

def f1(num):
    return num**2
def f2(x: int, y: float):
    return x - y
def f3(x: int, y: int, z: int):
    return x + y / z

def find_root(func, num1, num2):
    eps = 0.00001
    ans = num1
    while abs(func(ans)) >= eps:
        ans = derivative(func,ans)

    print(f'The root is: {ans}')
    return ans

def derivative(func,number): # Auxiliary function for finding the derivative
    return number - func(number) / (func(number+func(number)) - func(number))


if __name__ == '__main__':
    print("___Tests cases results___")
    find_root(lambda x: x * 2, 2, 6) # should return-> The root is: 0.0
    find_root(lambda x: x * 3, 0, 0) # should return-> The root is: 0
    find_root(lambda x: x + 2, 3, 8)  # should return-> The root is: -2.0
    find_root(lambda x: x + 3, 3, 8)  # should return-> The root is: -3.0
    find_root(lambda x: x - 4, 4, 4)  # should return-> The root is: 4
    find_root(lambda x: x / 5, 5, 5)  # should return-> The root is: -8.881784197001252e-16
    find_root(lambda x: x ** 2-4, -3, 1)  # should return-> The root is: -2.0
    print("\n___Tests cases results: Invalid input___")
    try:
        find_root(lambda x: x ** 2 , "aa", 1)  # should return-> unsupported operand type(s) for ** or pow(): 'str' and 'int'
    except:
        print("unsupported operand type(s) for ** or pow(): 'str' and 'int'")
    try:
        find_root(lambda x: x / 0, 4, 4)  # should return-> ZeroDivisionError: division by zero
    except:
        print("ZeroDivisionError: division by zero")
    try:
        find_root(lambda x: x * 2 , "aba", "1")  # should return-> bad operand type for abs(): 'str'
    except:
        print("bad operand type for abs(): 'str'")



    """
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))
    """