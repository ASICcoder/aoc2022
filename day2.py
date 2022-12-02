import re;

with open("input.txt") as f:
    data = [['r' if x == 'X' or x == 'A' else 'p' if x == 'Y' or x == 'B' else 's' for x in i if x != ' '] for i in f.read().strip().split("\n")]
    
a = list(map(lambda x: sum([1 if x[0] == 'r' else 2 if x[0] == 'p' else 3, 3 if x[0] == x[1] else 6 if ''.join(x) == 'rp' or ''.join(x) == 'ps' or ''.join(x) == 'sr' else 0]), data))
def c(o, w):
    if(o == 'r'):
        return (w == 'r') * 3 + (w == 'p') * 1 + (w == 's') * 2
    elif(o == 'p'):
        return (w == 'r') * 1 + (w == 'p') * 2 + (w == 's') * 3
    else:
        return (w == 'r') * 2 + (w == 'p') * 3 + (w == 's') * 1
b = list(map(lambda x: sum([0 if x[1] == 'r' else 3 if x[1] == 'p' else 6, c(x[0], x[1])]), data))
print(sum(a))
print(sum(b))

