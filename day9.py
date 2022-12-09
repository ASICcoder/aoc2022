with open("input.txt") as f:
    data = [str(i).split(' ') for i in f.read().strip().split("\n")]

def p(n):
    moves = []
    k = [[0,0] for i in range(n)]
    for m in data:
        for i in range(int(m[1])):
            k[0][0] += 1 * m[0]=='R'
            k[0][0] -= 1 * m[0]=='L'
            k[0][1] += 1 * m[0]=='U'
            k[0][1] -= 1 * m[0]=='D'

            for c in range(1,n):
                x = k[c-1][0] - k[c][0]
                y = k[c-1][1] - k[c][1]

                if (abs(x) > 1 or abs(y) > 1):
                    k[c] = [k[c][0] + (1 if x > 0 else -1 if x < 0 else 0) , k[c][1] + (1 if y > 0 else -1 if y < 0 else 0)]
            moves.append(k[n-1])
    return sum([1 for i in range(len(moves)) if moves[i] not in moves[i+1:]])

print(p(2))
print(p(10))

