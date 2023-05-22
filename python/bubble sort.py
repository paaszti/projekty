def BS(a):
    list=[]
    elements_list=len(list)
    for j in range (0, elements_list-1):
        for i in range (0,elements_list-1):
            if list[i]>list[i+1]:
                list[i], list[i+1] = list [i+1], list [i]
    return list