from functools import lru_cache

#@lru_cache()
'''

class bounded_subsets():
    def __init__(self, S, C, step = 1):
        self.step = step
        self.S = S
        self.C = C
        self.ans = []

    def __iter__(self):
        return self

    def __next__(self):
        return self

    @lru_cache()
    def limited_sets(self):
        
'''

class bounded_subsets():
    def __init__(self, S, C, step = 1):
        self.ans = get_subsets(S,C)
        print(self.ans)
        i = 5

    def get_subsets(data: list, target: int):
        # initialize final result which is a list of all subsets summing up to target
        subsets = []
        '''for i in range(target):
            subsets.append(i)'''
        for i in data:
            if i <= target:
                subsets.append(i)
        # records the difference between the target value and a group of numbers
        differences = {}

        for number in data:
            #prospects = []

            # iterate through every record in differences
            for diff in differences:

                # the number complements a record in differences, i.e. a desired subset is found
                if number - diff <= 0:
                    new_subset = [number] + differences[diff]
                    new_subset.sort()
                    if new_subset not in subsets:
                        subsets.append(new_subset)

                # the number fell short to reach the target; add to prospect instead
                '''elif number - diff < 0:
                    print("@@@@@@@@@@")
                    prospects.append((number, diff))'''

            # update the differences record
            '''for prospect in prospects:
                print("@@@@@@@@@@")
                new_diff = target - sum(differences[prospect[1]]) - prospect[0]
                differences[new_diff] = differences[prospect[1]] + [prospect[0]]'''
            differences[target - number] = [number]

        for i in range(len(subsets)):
            yield subsets[i]
        #for i in subsets:
         #   yield i



if __name__ == '__main__':
    list=[1,2,3]
    for s in bounded_subsets.get_subsets(list,5):
        print(s, end=', ')
    list = [1, 2, 3,4,5,6,7,8]
    print()
    for s in bounded_subsets.get_subsets(list,8):
        print(s, end= ', ')
    '''
    ans=get_subsets(list,4)
    print(next(ans))
    '''








