list=[]
x=int(input("Type a number and I'll check if it's a prime number: "))
if x>1:
    for i in range(1, x+1):
        if x%i==0:
            list.append(i)
if len(list)<=2 and len(list)!=0:
    print(f"{x} is a prime number!")
else:
    print(f"{x} is not a prime number :(")