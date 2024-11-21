def common_unpressed(one: list[list], two:list[list]) -> list[list]:
    """Returns the intervals in which both buttons were unpressed.
    This function assumes that both input lists are sorted, and the 
    timer starts at 0."""
    cur_t = 0
    one_pt, two_pt = 0, 0
    ints = []
    while one_pt < len(one) and two_pt < len(two):
        if one[one_pt][0] < two[two_pt][0]:
            if one[one_pt][0] > cur_t:
                ints.append([cur_t, one[one_pt][0]])
            cur_t = one[one_pt][1]
            one_pt += 1
        else:
            if two[two_pt][0] > cur_t:
                ints.append([cur_t, two[two_pt][0]])
            cur_t = two[two_pt][1]
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

print(common_unpressed([[0,4], [8,10]], [[2,6]]))

# [[0,4],[8,10]] and [[2,6]]