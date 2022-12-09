from functools import reduce
with open("input.txt") as f:
    data = [str(i) for i in f.read().strip().split("\n")]


dir_stack = ['/']
dirs = []
d = {'size' : 0}
fs = {'/' : {'size' : 0}}

for i in data:
    if i.startswith('$ cd '):
        print(dir_stack)
        if not i.endswith('..'):
            reduce(dict.get, dir_stack, fs)[i[5:]] =  {'size' : 0}
            dir_stack.append(i[5:])
        if i.endswith('..'):
            dir_stack.pop(-1)
    elif i.startswith('dir '):
        print('ignore dir')
    elif i.startswith('$ ls'):
        print('ignore ls')
    else:
        print(i)
        reduce(dict.get, dir_stack, fs)['size'] += int(i.split(' ')[0])

print(dir_stack)

def walk(x):
    if len(x.keys()) > 1:
        for i in x:
            if i != 'size':
                walk(x[i])
                x['size'] += x[i].get('size', 0)
    dirs.append(x['size'])

walk(fs['/'])
print(fs)
dirs.sort()
print(dirs)
def p1(x):
    b = 0
    for i in x:
        if i != 'size':
            b +=  p1(x[i])
    b += x['size'] if x['size'] <= 100000 else 0
    return(b)

print(p1(fs['/']))

print(fs['/']['size'])
a = [x for x in dirs if (70000000 - fs['/']['size'] + x) >= 30000000 ]
print(a)
