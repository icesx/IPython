import pandas as pd


def my_reduce(x,y):
    print(x,y)


if __name__ == '__main__':
    all = [("a",1),("a",2),("b",1),("c",1)]
    df = pd.DataFrame(all,columns=['A','B'])
    print(df)
    print(df.groupby(['A','B']).groups['a','b'])
