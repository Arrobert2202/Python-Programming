def x_times(*lists, x):
    times = {}
    final_list = []
    for list in lists:
        for a in list:
            if a in times:
                times[a] += 1
            else:
                times[a] = 1
    for a, val in times.items():
        if val == x:
            final_list.append(a)
    return final_list
print(x_times([1,2,3], [2,3,4], [4,5,6], [4,1, "test"], x = 2))