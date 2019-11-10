if __name__ == '__main__':
    head = 20
    feat = 46
    for chick in range(0,20):
        for rabbit in range(0,20 - chick):
            if chick * 2 + rabbit * 4 == 46:
                print('chick is',chick,'rabbit is ',rabbit)
                break
