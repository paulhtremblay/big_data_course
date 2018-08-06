def first_n_as_list(n):
    num = 0
    nums =  []
    while num < n:
        nums.append(num)
        num += 1
    return nums

s = sum(first_n_as_list(1000000))
print(s)

