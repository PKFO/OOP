x = [int(e) for e in input().split()]
x.sort()
temp = False
for i in range(len(x)):
    if x[i] == 0:
        temp = True
    elif x[i] > 0 and temp :
        x[0] = x[i]
        x[i] = 0
        break;
print("".join(map(str,x)))