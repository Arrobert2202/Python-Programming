def Sort_Tuple(list): 
    list.sort(key = lambda x: x[1][2]) 
    return list 
print(Sort_Tuple([('abc', 'bcd'), ('abc', 'zza')]))