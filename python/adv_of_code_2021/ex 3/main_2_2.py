list=[]
f = open('text2.txt', 'r')
for line in f:
    list.append(line)
zero = 0
one = 0
lenght = len(list)
for j in range (12):
    for i in range (lenght):
        if list[i][j] == '0':
            zero+=1
        else:
            one+=1
    i=0
    while i<lenght:
        if zero > one and list[i][j]=='1':
            list.remove(list[i])
            i -= 1
            lenght=len(list)
        elif one >= zero and list[i][j]=='0':
            list.remove(list[i])
            i-=1
            lenght=len(list)
        else:
            i+=1
            lenght=len(list)
    zero = 0
    one = 0
    if lenght == 2:
        list.remove(list[1])
        break
list_1=list[0][:12]
x=int(list_1, 2)
list=[]
f = open('text2.txt', 'r')
for line in f:
    list.append(line)
zero = 0
one = 0
lenght = len(list)
for j in range (12):
    for i in range (lenght):
        if list[i][j] == '0':
            zero+=1
        else:
            one+=1
    if lenght == 2:
        list.remove(list[0])
        break
    i=0
    while i < lenght:
        if zero <= one and list[i][j] == '1':
            list.remove(list[i])
            i -= 1
            lenght = len(list)
        elif one < zero and list[i][j] == '0':
            list.remove(list[i])
            i -= 1
            lenght = len(list)
        else:
            i += 1
            lenght = len(list)
    zero = 0
    one = 0
    if lenght == 2:
        list.remove(list[1])
        break
list_2=list[0][:12]
z=int(list_2, 2)
print(f'The oxygen generator rating is: {x}')
print(f'The CO2 scrubber rating is: {z}')
print(f'The life support rating of the submarine is: {z*x}')
f.close()