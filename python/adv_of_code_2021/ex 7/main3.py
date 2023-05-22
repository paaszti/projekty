with open("input.txt") as f:
    data = [int(x) for x in f.read().strip().split(",")]
    part_one = min([ sum([max([x,i]) - min([x,i]) for x in data]) for i in range(min(data), max(data))])
    part_two = min([ sum([ sum(range(1 + max([x,i]) - min([x,i]))) for x in data]) for i in range(min(data), max(data))])
print(part_one)
print(part_two)