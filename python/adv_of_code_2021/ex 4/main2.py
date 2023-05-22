list=[3,4,3,1,2]
lenght=len(list)
for j in range(80):
    for i in range(lenght):
        list[i]=list[i]-1
        for z in range(lenght):
             if list[i]==-1:
                 list[i]=6
                 list.append(8)
    lenght=len(list)
print(list)
print(lenght)