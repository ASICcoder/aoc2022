with open("input.txt") as f:
    data = [str(i) for i in f.read().strip().split("\n")]
    
cal = [0]
for d in data:
    if d != '':
        cal[-1] += int(d)
    else:
        cal.append(0)
cal.sort(reverse = True)  
print(cal[0])      
print(sum(cal[:3]))
