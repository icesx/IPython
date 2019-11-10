from functools import reduce


def my_map(x):
    return x * 2 + 10


def my_reduce(x,y):
    return x + y


def my_filter(x):
    return x % 3 == 0


if __name__ == '__main__':
    all = list(range(1,10))
    print(reduce(my_reduce,all))
    print(map(my_map,all))
    print(filter(my_filter,all))
