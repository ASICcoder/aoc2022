import itertools
with open("input.txt") as f:
    data = [str(i) for i in f.read().split("\n")]
    
    
stack, steps = [list(y) for x, y in itertools.groupby(data, lambda z: z == '') if not x]
stack.pop()

a = list(zip(*[[i[a:a+3] for a in range(0, len(i), 4)] for i in stack]))
a = [[i[1] for i in x if i != '   '] for x in a]
b = [[int(x[1]), int(x[3])-1, int(x[5])-1] for x in (i.split(' ') for i in steps)]


for i in b:
    print(i)
    temp = a[i[1]][:i[0]]
    #temp.reverse() #For p1
    a[i[1]] = a[i[1]][i[0]:]
    temp.extend(a[i[2]])
    a[i[2]] = temp
    print(a)


p1 = ''
for i in a:
    p1 += i[0]

print(p1)
