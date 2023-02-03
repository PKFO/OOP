dict = {3:4, 5:6, 7:8}
def is_plusone_dictionary(d):
    count = False
    total = 0
    for i in d.keys():
        if d[i] - i == 1 and count == False:
            total += 1
            before = d[i] + i 
            count = True
        if (d[i] + i) - before == 4 and count == True:
            before = d[i] + i
            total += 1
    if total == len(d):
        return print('True')
    else:
        return print('False')
is_plusone_dictionary(dict)

    
