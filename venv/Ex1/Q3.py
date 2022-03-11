import doctest

"""
Newton's method:  find_root -> this function gets a function and two real numbers,
and finds its root in the defined domain by the numbers. 
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
    find_root(lambda x: x**2-4, 1, 3)
    find_root(lambda x: x**2-4, -3, -1)
    find_root(lambda x: x**2-4, -3, 1)
    find_root(lambda x: x ** 2 - 4, 1, 3)
    find_root(lambda x: x ** 2 - 4, -3, -1)
    find_root(lambda x: x ** 2 - 4, -3, 1)