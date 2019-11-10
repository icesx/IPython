def la_01(x):
    return lambda y,z: y * x + z


if __name__ == '__main__':
    '''5*2+1
    la_01(5)=def la_01(y,z):y*5+z'''
    print(la_01(5)(2,1))
