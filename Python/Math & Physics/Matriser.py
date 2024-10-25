import numpy as np

T1 = np.array([[1, 3, 7],[2, 4, 0]])
T2 = np.array([[3, 2],[5,1],[5,1]])
A = np.array([[-2, -1],[12, -9]])
B = np.array([[2, 3],[5, 7]])
C = np.array([[6, 1, -9],[1, 0, 1]])


# PARAMETRE
arr1 = T1
arr2 = T2

arr1rows = len(arr1)
arr1cols = len(arr1[0])
arr2rows = len(arr2)
arr2cols = len(arr2[0])

def product():
    if (arr1cols == arr2rows):
        arrOut = np.array([[0]*arr2cols for i in range(arr1rows)])
        for i in range(arr1rows):
            for j in range(arr2cols):
                addSum = 0
                for n in range(arr1cols):
                    addSum += arr1[i,n] * arr2[n,j]
                    
                arrOut[i,j] = addSum
        print(arr1, "\n*\n", arr2, "\n=\n", arrOut)
    else:
        print("Columns of A has to match rows of B, could not do operation")
        
def add():
    if ((arr1rows == arr2rows) and (arr1cols == arr2cols)):
        arrOut = np.array([[0]*arr2cols for i in range(arr1rows)])
        for i in range(arr1rows):
            for j in range(arr2cols):
                arrOut[i, j] = arr1[i,j] + arr2[i, j]
        print(arr1, "\n+\n", arr2, "\n=\n", arrOut)
    else:
        print("Columns and rows has to match, could not do operation")

def subtract():
    if ((arr1rows == arr2rows) and (arr1cols == arr2cols)):
        arrOut = np.array([[0]*arr2cols for i in range(arr1rows)])
        for i in range(arr1rows):
            for j in range(arr2cols):
                arrOut[i, j] = arr1[i,j] - arr2[i, j]
        print(arr1, "\n-\n", arr2, "\n=\n", arrOut)
    else:
        print("Columns and rows has to match, could not do operation")

product()