

def bounded_subsets(S, C):
    count_index = 0
    max_permotations = 2**len(S)
    one_dimension_set = []
    candidate_sets = {}
    final_sets = [[]]
    S.sort()
    for i in range(len(S)):
        if S[i] <= C:
            one_dimension_set.append(S[i])
            candidate_sets[S[i]]=[S[i]]
            final_sets.append([S[i]])
        else:
            break
    print(one_dimension_set)
    print(candidate_sets)
    print(final_sets)

    while candidate_sets != {}:
        for num in one_dimension_set:
            for j in range(count_index):
                sum = one_dimension_set[j] + num:



if __name__ == '__main__':
    bounded_subsets([6,1,2,5,3,1],8)