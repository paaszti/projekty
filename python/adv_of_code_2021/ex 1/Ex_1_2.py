list=[]
f = open('numbers.txt', 'r')
for line in f:
    list.append(line)
new_list=[int(j) for j in list]
lenght=len(new_list)
list2=[]
increased = 0
for i in range(lenght):
    if i <= 1997:
        list2.append((new_list[i]+new_list[i+1]+new_list[i+2]))
for i in range(len(list2)):
        if list2[i] > list2[i-1]:
            increased+=1
print(increased)
