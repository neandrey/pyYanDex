arg1 = [1,2,3]
arg2 = ['bob', 'tom', 'ret', 'sem', 'dilan']

def func(arg1, arg2):
    rets = {}
    for i in arg1:
        if arg2 == []:
            rets[i] = None
        for j in arg2:
            rets[i] = j
            arg2 = arg2[1:]
            break
    return rets


if __name__ == '__main__':
    R = func(arg1, arg2)
    print(R)