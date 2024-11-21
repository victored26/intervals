def common_unpressed(one: list[list], two:list[list]) -> list[list]:
    """Returns the intervals in which both buttons were unpressed.
    This function assumes that both input lists are sorted, and the 
    timer starts at 0."""
    cur_t = 0
    one_pt, two_pt = 0, 0
    ints = []
    while one_pt < len(one) and two_pt < len(two):
        equal_case = one[one_pt][0] == two[two_pt][0]
        equal_case = equal_case and one[one_pt][1] <= two[two_pt][1]

        if one[one_pt][0] < two[two_pt][0] or equal_case:
            if one[one_pt][0] > cur_t:
                ints.append([cur_t, one[one_pt][0]])
            cur_t = max(cur_t, one[one_pt][1])
            one_pt += 1

        else:
            if two[two_pt][0] > cur_t:
                ints.append([cur_t, two[two_pt][0]])
            cur_t = max(cur_t, two[two_pt][1])
            two_pt += 1

    while one_pt < len(one):
        if one[one_pt][0] > cur_t:
            ints.append([cur_t, one[one_pt][0]])
        cur_t = one[one_pt][1]
        one_pt += 1
    
    while two_pt < len(two):
        if two[two_pt][0] > cur_t:
            ints.append([cur_t, two[two_pt][0]])
        cur_t = two[two_pt][1]
        two_pt += 1

    return ints

# My test cases
"""assert(common_unpressed([[0,4], [8,10]], [[2,6]]) == [[6,8]])
assert(common_unpressed([[2,6]], [[0,4], [8,10]]) == [[6,8]])
assert(common_unpressed([[0,4]], [[2,3]]) == [])
assert(common_unpressed([[2,3]], [[0,4]]) == [])
assert(common_unpressed([[0,1], [7,10]], [[0,2], [3,5]]) == [[2,3], [5,7]])
assert(common_unpressed([[0,1], [7,10]], [[1,2], [3,5]]) == [[2,3], [5,7]])
assert(common_unpressed([[0,3], [4,6]], [[1,2], [3,4]]) == [])
assert(common_unpressed([[0,2], [5,9], [12, 13]], [[1,2], [8,9]]) == [[2,5], [9, 12]])
assert(common_unpressed([[0,1]], [[9,10]]) == [[1,9]])
assert(common_unpressed([[1,2], [5,6], [11,13]], [[0,3], [5,7], [8,10]]) == [[3,5], [7,8], [10, 11]])"""