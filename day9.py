matrix = []

# with open("day9_short.txt", "r") as f:
with open("day9.txt", "r") as f:
    lines = f.readline()
    while lines:
        line=(lines.strip("\n"))
        matrixline=[int(x) for x in line]
        matrix.append(matrixline)
        lines = f.readline()

def GetValue(matrix,x,y):
    if x < 0 or x >= len(matrix):
        return(10)
    if y < 0 or y>=len(matrix[0]):
        return(10)
    return matrix[x][y]

total=0
for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        count=0
        offsets = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        for offset in offsets:
            if matrix[x][y] < GetValue(matrix, offset[0], offset[1]):                
                count+=1
            if count == 4:
                # print(matrix[x][y])
                total += (1+ matrix[x][y])
print(total)


# for y,line in enumerate(matrix):
#     for x,value in enumerate(line):
#         if value < matrix[x+1][y]: 
#             print(value)
#         if value < matrix[x][y+1]:
#             print(value)
#         if value < matrix[x-1][y]: 
#             print(value)
#         if value < matrix[x][y-1]:
#             print(value)
        


