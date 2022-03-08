'''
כתבו מבנה בשם List ,שהוא זהה לרשימה של פייתון (list),אבל מאפשר לגשת לפריטים בתחביר של מערך רב -ממדי
'''

class List(list):
    def __init__(self,list):
        super().__init__(list)

    def __getitem__(self, item):
        if type(item) is tuple and len(item) == 3: #3D
            row_index = item[0]
            arr_index = item[1]
            element_index = item[2]
            row = super().__getitem__(row_index)  # == list[row_index]
            arr = row[arr_index]
            element = arr[element_index]
            # print(f'row={row},arr={arr},element={element}')
            return element
        elif type(item) is tuple and len(item) == 2: #2D
            row_index = item[0]
            arr_index = item[1]
            row = super().__getitem__(row_index)  # == list[row_index]
            element = row[arr_index]
            return element
        else:
            return super().__getitem__(item) #1D

    def __setitem__(self, key, value):
        if type(key) is tuple and len(key) == 3: #3D
            row_index = key[0]
            arr_index = key[1]
            element_index = key[2]
            row = super().__getitem__(row_index)  # == list[row_index]
            arr = row[arr_index]
            arr[element_index] = value
            return
        elif type(key) is tuple and len(key) == 2: #2D
            row_index = key[0]
            arr_index = key[1]
            row = super().__getitem__(row_index)  # == list[row_index]
            row[arr_index] = value
            return
        else:
            super().__setitem__(key, value) #1D
            return


if __name__ == '__main__':
    l=List([
        [[1,2,3,4],[5,6,7,8]],
        [[5, 6, 7, 8], [9, 10, 11, 12]],
        [[13, 14, 15, 16], [17, 18, 19, 20]],
        ]
    )
    print(l[0,1,3])
    print(l[0,1])
    l[0,1]=["aaaaa"]
    print(l[0,1])
    l[1,1,1]="bbb"
    print(l[1,1,1])
    print(l[0])
    l1 = List([
        [[[1, 2, 3, 4], [5, 6, 7, 8]]],
        [[[5, 6, 7, 8], [9, 10, 11, 12]]],
        [[[13, 14, 15, 16], [17, 18, 19, 20]]],
        [[['13', '14', 'a', 16], [17, 18, 19, 20]]],
    ]
    )
    print(l1[3, 0, 1])
    print(l1)
