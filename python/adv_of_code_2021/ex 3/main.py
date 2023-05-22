list=[]
gamma_rate = []
f = open('text2.txt', 'r')
for line in f:
    list.append(line)
lenght = len(list)
zero = 0
one = 0
for j in range (12):
    list_0 = []
    for i in range (lenght):
        list_0.append(int(list[i][j]))
    for item in list_0:
        if item == 0:
            zero+=1
        else:
            one+=1
    if zero > one:
            gamma_rate.append(0)
    else:
        gamma_rate.append(1)
    zero = 0
    one = 0
strings = [str(integer) for integer in gamma_rate]
a_string = "".join(strings)
an_integer = int(a_string, 2)
x=len(a_string)
epsilon_rate=[]
final_epsilon_rate = []
for i in range(x):
    if a_string[i]=='0':
        epsilon_rate.append(a_string.replace("0", "1"))
    else:
        epsilon_rate.append(a_string.replace("1", "0"))
a_integer="".join(epsilon_rate)
an_integer2=int(a_integer)
for i in range (len(epsilon_rate)):
    final_epsilon_rate.append(epsilon_rate[i][0])
strings_1 = [str(integer_1) for integer_1 in final_epsilon_rate]
a_string_1 = "".join(strings_1)
an_integer_1 = int(a_string_1, 2)
print(an_integer*an_integer_1)
f.close()
