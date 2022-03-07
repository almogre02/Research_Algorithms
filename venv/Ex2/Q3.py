'''
כתבו מבנ ה בשם List ,שהוא זהה לרשימה של פייתון (list),אבל מאפשר לגשת לפריטים בתחביר של מערך רב -ממדי
'''


class List(list):
    def __getitem__(self, item):
        if type(item) is int:
            return super().__getitem__(item)
        else:
            row_index=item[0]
            arr_index=item[1]
            element_index=item[2]
            row=super().__getitem__(row_index) # == list[row_index]
            arr=row[arr_index]
            element=arr[element_index]
            #print(f'row={row},arr={arr},element={element}')
            return element



if __name__ == '__main__':
    l=List([
        [[1,2,3,4],[5,6,7,8]],
        [[5, 6, 7, 8], [9, 10, 11, 12]],
        [[13, 14, 15, 16], [17, 18, 19, 20]],
        ]
    )
    print(l[0,1,3])
    print(l[0])