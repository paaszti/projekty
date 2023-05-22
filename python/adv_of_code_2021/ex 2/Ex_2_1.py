forward = []
forward_1 = 0
down = []
down_1 = 0
up = []
up_1 = 0
f = open('test.txt', 'r')
for line in f:
    if line[:7] == 'forward':
        forward.append(line)
    elif line[:4] == 'down':
        down.append(line)
    else:
        up.append(line)
for i in range (len(forward)):
    x=(forward[i])
    z=int(x[8:])
    forward_1+=z
for i in range (len(down)):
    x1=(down[i])
    z1=int(x1[5:])
    down_1+=z1
for i in range (len(up)):
    x2=(up[i])
    z2=int(x2[3:])
    up_1+=z2
depth = down_1 - up_1
finals_positions = forward_1 * depth
g=f"Depth = {depth} and mulitply = {finals_positions}"
f.close()
with open('result.txt', 'w') as file:
    file.write(g)