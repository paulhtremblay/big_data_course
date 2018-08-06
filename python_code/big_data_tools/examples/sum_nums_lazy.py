def first_n_as_lazy(n):
    num = 0
    while num < n:
        yield num
        num += 1

s  = sum(first_n_as_lazy(1000000))
print(s)
