with open("input.txt") as f:
    data = [str(i) for i in f.read().strip().split("\n")]

a = list(zip(*[list(i) for i in data]))
a = [''.join(i) for i in a]

def vis(x,y):
    if (x==0 or y==0 or x==len(data)-1 or y==len(data)-1) or \
       (data[y].find(max(data[y][:x+1])) == x) or \
       ((data[y].rfind(max(data[y][x:])) == x) and (data[y].rfind(max(data[y][x:])) != data[y].find(max(data[y][:x+1])))) or \
       (a[x].find(max(a[x][:y+1])) == y) or \
       ((a[x].rfind(max(a[x][y:])) == y) and (a[x].rfind(max(a[x][y:])) != a[x].find(max(a[x][:y+1])))):
        return True
    else:
        return False
s = 0
for j in range(len(data)):
    s += sum([int(vis(i,j)) for i in range(len(data))])

print(s)

def duh(xx,d):
    sum = 0
    for  i in range(xx-1,-1,-1):
        sum += 1
        if  xx==1 or d[i] >= d[xx]:
            break
    return sum
    # LOL :D return [d[i] for i in range(xx-1,-1,-1) if  xx==1 or (xx-i==1 and d[xx]==d[i]) or d[i:xx].rfind(max(d[i:xx]))==0 or (d[i:xx].rfind(max(d[i:xx]))==1 and d[0]==d[1])]

def cnt(x,y):
    return duh(x,data[y]) * duh(len(data)-x-1, data[y][::-1]) * duh(y,a[x]) * duh(len(data)-y-1, a[x][::-1])

score = []
for j in range(1,len(data)-1):
    for i in range(1,len(data)-1):
        score.append(cnt(i,j))
print(sorted(score)[-1])
