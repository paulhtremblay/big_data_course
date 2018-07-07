def firstn(n):
    num = 0
    nums =  []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))

