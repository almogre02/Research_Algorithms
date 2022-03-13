import doctest
"""
Write a function called print_sorted, which receives as input a deep data structure consisting of lists, tuple, set,
dict and prints it when it is arranged at all levels (values in lists, handles and groups)
Arranged in ascending order; The entries in the dictionary are arranged in ascending order of the keys.
"""
def print_sorted(data_structure):
    sorted_keys=sorted(data_structure) # returns the Data_structure keys by ascending order
    sorted_dict={}
    for key in sorted_keys:
        if data_structure[key].__class__ == (tuple or set or dict or list):
            for value in data_structure[key]:
                inner_sort = sorted(value)
                #sorted_dict[key]=sorted(data_structure[key])
                sorted_dict[key] = inner_sort
        else:
            sorted_dict[key] = data_structure[key]


    print(f'The sorted structure is:{sorted_dict}')
    return sorted_dict

if __name__ == '__main__':
    before = {"a": 5, "c": 6, "b": [1, 2, 3, 4]}
    print(f'before sort:{before} , after sort:{print_sorted(before)}')


