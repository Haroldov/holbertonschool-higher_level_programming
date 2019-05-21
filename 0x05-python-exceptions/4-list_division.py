#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = 0
    div = []
    for index in range(list_length):
        try:
            res =  my_list_1[index] / my_list_2[index]
        except IndexError:
            res = 0
            print("out of range")
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        finally:
            div.append(res)
    return div
