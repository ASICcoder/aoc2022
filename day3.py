with open("input.txt") as f:
    #data = [ [ord(x) - 96 if x.islower() else ord(x) - 64 for x in i] for i in f.read().strip().split("\n")]
    data = [ [x for x in i] for i in f.read().strip().split("\n")]
    
a = [(list(set(i[:len(i)//2]).intersection(i[len(i)//2:]))) for i in data]
b = [[ord(x) - 96 if x.islower() else ord(x) - 64 + 26 for x in i] for i in a]
c = [i for n in b for i in n]

print(sum(c))

g = list(zip(*(iter(data),) * 3))
def badge(x):
    r = set(x[0])
    for y in x[1:]:
        r.intersection_update(set(y))
    return list(r)
h = [badge(x) for x in g]
q = [i for n in h for i in n]
b = [ord(x) - 96 if x.islower() else ord(x) - 64 + 26 for x in q]

print(sum(b))
