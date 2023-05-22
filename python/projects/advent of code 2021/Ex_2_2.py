with open('test.txt') as data:
    list = [i.strip() for i in data.readlines()]
aim = 0
depth = 0
horizontal = 0
for i in list:
    if "forward" in i:
        depth += int(i[8:])*aim
        horizontal += int(i[8:])
    elif "down" in i:
        aim += int(i[5:])
    elif "up" in i:
        aim -= int(i[3:])
print(f"Third value is {depth*horizontal}")




