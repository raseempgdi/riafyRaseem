import numpy as np

def countElement(array,element):
    array1 = np.array(array)
    count = (array1 == element).sum() - 1
    return count


array=[[[8,2,5,5,9],[3,8,1,1,0],[6,1,1,9,0],[6,3,1,6,1],[1,2,9,8,8]],[[3,5,5,7,6],[1,4,1,7,7],[0,9,4,9,6],[6,1,5,3,5],[5,8,3,8,6]],[[4,3,0,8,5],[1,9,4,2,5],[1,7,4,2,0],[8,3,6,4,5],[3,5,0,5,4]],[[2,6,9,0,1],[5,9,6,3,7],[2,2,4,3,9],[4,9,7,6,4],[1,5,3,5,5]],[[8,1,2,3,5],[2,6,7,8,5],[7,3,7,1,3],[3,1,5,7,7],[2,8,3,2,9]]]
element = int(input("which number count you want to find :"))
print(countElement(array,element))