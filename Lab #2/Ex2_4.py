def count_minus(str):
    new = [int(e) for e in str.split()]
    return sum([1 for i in new if i < 0])
