# Program to add two matrices using nested loop
def swapPositions(list, pos1, pos2):
    if (pos1 >= 0 and pos1 < (len(list))) and (pos2 >= 0 and pos2 < (len(list))):
        list[pos1], list[pos2] = list[pos2], list[pos1]
        return list
    else:
        return print('error') 
 
# Driver function
List = ['i', 'love','you','na']
pos1, pos2  = 4,1 
print(len(List))
print(swapPositions(List, pos1-1, pos2-1))





