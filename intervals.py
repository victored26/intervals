def common_intervals(list_one: list[list], list_two:list[list]) -> list[list]:
    """Returns the intervals in which both buttons were unpressed.
    This function assumes that both input lists are sorted, and the 
    timer starts at 0."""
    fin_t = max(list_one[-1][1], list_two[-1][1])
    unpr_one = unpressed_intervals(list_one, fin_t)
    unpr_two = unpressed_intervals(list_two, fin_t)
    res = []
    two_pt = 0
    for one_pt in range(len(unpr_one)):
        if unpr_one[one_pt][1] < unpr_two[two_pt][0]:
            continue

        end_interval = unpr_one[one_pt][1]
        while two_pt < len(unpr_two) and unpr_two[two_pt][0] <= unpr_one[one_pt][1]:
            end_interval = min(end_interval, unpr_two[two_pt][1])
            two_pt += 1
        
        res.append([unpr_one[one_pt][0], end_interval])
    return res


def unpressed_intervals(list_one: list[list], fin_t: float) -> list[tuple]:
    """Returns the intervals of which the button was unpressed.
    This function assumes that the list argument is sorted, and the 
    timer starts at 0 and ends at t_f."""
    res = []
    cur_t = 0
    for j in range(len(list_one)):
        time_pressed = list_one[j][0]
        time_released = list_one[j][1]
        if cur_t != time_pressed:
            res.append((cur_t, time_pressed))
        cur_t = time_released
    if cur_t < fin_t:
        res.append((cur_t, fin_t))
    return res
