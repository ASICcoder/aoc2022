import itertools
with open("input.txt") as f:
    data =  f.read().strip()

def parse(n):
    for i in range(0, len(data)-n-1):
        if(sum([1 for x in data[i:i+n] if data[i:i+n].count(x) > 1])==0):
            return(i+n)
            
print(parse(4))
print(parse(14))

