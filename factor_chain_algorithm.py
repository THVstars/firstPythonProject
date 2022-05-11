def factor_chain(lst):
    return lst[-1] % lst[-2] == 0
    # all([lst[-1] % num == 0 for num in lst[:-1]]) better solution.


print(factor_chain([1, 2, 4, 8, 16]))
