#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    def division(x, y): return x / y if y != 0 else 0
    resultList = []

    for item in range(list_length):
        try:
            dataList1 = my_list_1[item]
            dataList2 = my_list_2[item]
            resultList.append(division(dataList1, dataList2))
        except ZeroDivisionError:
            print("division by 0")
            resultList.append(0)

        except TypeError:
            print("wrong type")
            resultList.append(0)

        except IndexError:
            print("out of range")
            resultList.append(0)

    return resultList
