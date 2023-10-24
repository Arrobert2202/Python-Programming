def tuple_lists(*lists):
    max_length = max(len(x) for x in lists)
    tuples = []
    for i in range(max_length):
        merged_tuple = tuple(x[i] if i < len(x) else None for x in lists)
        tuples.append(merged_tuple)

    return tuples
print(tuple_lists([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))