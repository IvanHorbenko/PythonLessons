def common_elements():

    divide_by_3  = {v for v in range(100) if v % 3 == 0}
    divide_by_5  = {v for v in range(100) if v % 5 == 0}


    result = divide_by_3 & divide_by_5

    return result

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ОК')