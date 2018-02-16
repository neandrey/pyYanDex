
def valid_input(a):
    '''
    Проверяем входные значения на valid.
    '''
    for i in a:
        if (i % 1) == 0:
            continue
        else:
            print('Argument not integer')
            raise ValueError()

def minimum(a):
    '''
    Нахождение минимльных значений.
    '''
    minArg = []
    for i in range(2):
        temp = min(a)
        a.remove(min(a))
        minArg.append(temp)

    return minArg

def min_sum(a):
    '''
    Сумирование двух минимальных значений.
    '''
    sum = 0
    for i in a:
        sum += i

    return sum

if __name__ == '__main__':
    a = [1, 2, 3, 4, -1]
    valid_input(a)
    a = minimum(a)
    print(min_sum(a))
