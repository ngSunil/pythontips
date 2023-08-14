# map
from functools import reduce
mylist = [1, 2, 3, 4, 5]


def add(x):
    return x*2


print(list(map(add, mylist)))

# filter
mylist = [1, 2, 3, 4, 5]


def filterFunction(x):
    if x % 2 == 0:
        return x


print(list(filter(filterFunction, mylist)))


mylist = [1, 2, 3]


def reduce_sum(x, y):
    return x+y


print(reduce(reduce_sum, mylist))
