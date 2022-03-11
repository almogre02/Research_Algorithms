import inspect
import doctest
import math


def f1(x: int):
    return x ** 2
def f2(x: int, y: float):
    return x - y
def f3(x: int, y: int, z: int):
    return x + y / z


"""
The function accepts another function with arguments and activates the function 
only if the arguments are appropriate
return F result.
"""


def safe_call(func, *args,**kwargs):
    """
    >>> safe_call(f1,4)
    16
    >>> safe_call(f2,1,3)
    -1
    >>> safe_call(f3,1,3,2*2,7)
    6
    >>> safe_call(f3,1-3,3,3.5,0)
    -9.5
    >>> safe_call(f2,1-3,3,3.5,0)
    -9.5
    >>> safe_call(f1,1,"a",3.5,1)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(f,1,"fff",3.5,"qq")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(f,1,"2",3.5,"7")
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    >>> safe_call(f,'1',2,3.5,7)
    Traceback (most recent call last):
    Exception: The argument type doesn't fit the function annotations
    """
    annotations = []
    f_doc = inspect.getfullargspec(func)
    args_counter = len(f_doc.args)
    elements_counter = len(args)

    for i in range(args_counter):
        if f_doc.args[i] not in f_doc.annotations:
            annotations.append(None)
        else:
            annotations.append(f_doc.annotations.get(f_doc.args[i]))

    for i in range(elements_counter):
        if annotations[i] != None and type(args[i]) != annotations[i]:
            raise Exception("Annotations doesn't match")
            continue
    return func(*args)


if __name__ == '__main__':
    (failures, tests) = doctest.testmod(report=True)
    print("{} failures, {} tests".format(failures, tests))