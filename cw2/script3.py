def f1(lista, fun):
    li = []
    for i in list:
        if (fun(i)):
            li.append(i)
    return li

def fun(param):
    return param % 2 == 0

list = [1,4,6,2,3]

a = f1(list,fun())

