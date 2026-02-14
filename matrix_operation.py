"""

mat=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(mat[0][1])
for i in mat:
    for j in i:
        print(j,end=" ")
    print()
"""
"""
# Input matrix from user
print(list(range(2)))
mats=[]
for row in range(5):
    rows = []
    for col in range(3):
        value = int(input("Enter a number:"))
        rows.append(value)
    mats.append(rows)

print(mats)
"""

"""

# matrix summation
A = [[1,2,3],
 [4,5,6],
 [7,8,9]]
B=[[1,2,3],
 [4,5,6],
 [7,8,9]]
result=[[0,0,0],
       [0,0,0],
       [0,0,0]]
for i in range(3):
    for j in range(3):
        result[i][j] = A[i][j] + B[i][j]

print(result)
"""
# for multiplication
A = [[1,2,3],
 [4,5,6],
 [7,8,9]]
B=[[1,2,3],
 [4,5,6],
 [7,8,9]]
result1=[[0,0,0],
       [0,0,0],
       [0,0,0]]
rows =   len(A)
cols = len(A[0])
for x in range(rows):
    for y in range(cols):
        for k in range(rows):
            result1[x][y] += A[x][k] * B[k][y]

print(result1)
