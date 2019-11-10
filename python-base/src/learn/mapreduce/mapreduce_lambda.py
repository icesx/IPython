from functools import reduce

if __name__ == '__main__':
    all = list(range(1,10))
    print((reduce(lambda x,y: x + y,all)))
    print((list(map(lambda x: x * 2 + 10,all))))
    print((list(filter(lambda x: x % 3 == 0,all))))
