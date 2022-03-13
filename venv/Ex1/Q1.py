import doctest
import inspect
"""
Write a function called call_safe, which receives as input another function and arguments with names,
and calls the function with the arguments, but only they fit exactly to the types defined in the annotation of the function
"""


"""
Simple functions for tests
"""
def f1(x: int):
    return x * 2
def f2(x: int, y: float):
    return x - y
def f3(x: int, y: int, z: int):
    return x + y / z



def safe_call(func, *args,**kwargs):
    """
    >>> safe_call(f1,4)
    8
    >>> safe_call(f1,0)
    0
    >>> safe_call(f1,-2)
    -4
    >>> safe_call(f1,8*4-2)
    60
    >>> safe_call(f1,"aba")
    Traceback (most recent call last):
    Exception: Annotations doesn't match
    >>> safe_call(f1,"4")
    Traceback (most recent call last):
    Exception: Annotations doesn't match
    >>> safe_call(f2,1,3)
    Traceback (most recent call last):
    Exception: Annotations doesn't match
    >>> safe_call(f3,1,3,8)
    1.375
    >>> safe_call(f3,1,8,0)
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
    >>> safe_call(f3,"1","3",1)
    Traceback (most recent call last):
    Exception: Annotations doesn't match
    >>> safe_call(f1,3*5-2)
    26
    >>> safe_call(f1,2**2+47*3)
    290
    >>> safe_call(f3,2**2,4+8,5*3)
    4.8
    >>> safe_call(f2,"search","algorithms")
    Traceback (most recent call last):
    Exception: Annotations doesn't match
    >>> safe_call(f3,"search","algorithms","course")
    Traceback (most recent call last):
    Exception: Annotations doesn't match
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