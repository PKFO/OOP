def delete_minus(x):
    new = [[ y for y in i if y >= 0 ]for i in x]
    return new