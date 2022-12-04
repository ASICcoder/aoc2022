with open("input.txt") as f:
    data = [[[int(k) for k in j.split('-')] for j in str(i).split(',')] for i in f.read().strip().split("\n")]


s = [int(all(items in range(i[0][0], i[0][1] + 1) for items in range(i[1][0], i[1][1] + 1)) or all(items in range(i[1][0], i[1][1] + 1) for items in range(i[0][0], i[0][1] + 1))) for i in data]

print(sum(s))

s = [int(any(items in range(i[0][0], i[0][1] + 1) for items in range(i[1][0], i[1][1] + 1)) or any(items in range(i[1][0], i[1][1] + 1) for items in range(i[0][0], i[0][1] + 1))) for i in data]

print(sum(s))
