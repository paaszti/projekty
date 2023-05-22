list=[]
f = open('numbers.txt', 'r')
    for line in f:
        list.append(list)
new_list=[int(j) for j in list]
sum=0
lenght = len(list)
for i in range(lenght-1):
    if list[i + 1] > list[i]:
        sum += 1
x = f"The measure increased: {sum}"
with open('test.txt', 'w') as file:
     file.write(x)
