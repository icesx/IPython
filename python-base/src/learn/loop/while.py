# Copyright (C)
# Author: I
# Contact: 12157724@qq.com
def stand():
    count = 0
    while (count < 9):
        print('The count is:',count)
        count = count + 1

    print("Good bye!")


def sample():
    flag = 1

    while (flag): print('Given flag is really true!')

    print("Good bye!")


def while_else():
    count = 0
    while count < 5:
        print(count," is  less than 5")
        count = count + 1
    else:
        print(count," is not less than 5")


if __name__ == '__main__':
    sample()
    while_else()
    stand()
