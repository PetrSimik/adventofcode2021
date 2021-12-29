matrix = []

with open("day9.txt", "r") as f:
    lines = f.readline()
    while lines:        
        matrix.append(lines)
        lines = f.readline()
heightmap = matrix

# print(heightmap)

# heightmap = read_file("09.txt")

heightmap = [[0 if num !="9" else 9 for num in line.strip() ] for line in heightmap ]
width = len(heightmap[0])
height = len(heightmap)

def floodfill(matrix, x, y):
    score = 0
    if matrix[y][x] == 0:  
        matrix[y][x] = 1 
        score = 1
        if x > 0:
            score += floodfill(matrix,x-1,y)
        if x < len(matrix[0]) - 1:
            score += floodfill(matrix,x+1,y)
        if y > 0:
            score += floodfill(matrix,x,y-1)
        if y < len(matrix) - 1:
            score += floodfill(matrix,x,y+1)
    return score

scores = []
for idx in range(width):
    for jdx in range(height):
        scores.append(floodfill(heightmap, idx, jdx))

scores = sorted(scores, reverse=True)[:3]

print(f"Total: {scores[0] * scores[1] * scores[2]}")



# matrix = []

# with open("day9_short.txt", "r") as f:
# # with open("day9.txt", "r") as f:
#     lines = f.readline()
#     while lines:
#         line=(lines.strip("\n"))
#         matrixline=[int(x) for x in line]
#         matrix.append(matrixline)
#         lines = f.readline()

# def GetValue(matrix,x,y):
#     if x < 0 or x >= len(matrix):
#         return(10)
#     if y < 0 or y>=len(matrix[0]):
#         return(10)
#     return matrix[x][y]

# total=0
# for x in range(len(matrix)):
#     for y in range(len(matrix[0])):
#         count=0
#         offsets = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
#         for offset in offsets:
#             if matrix[x][y] < GetValue(matrix, offset[0], offset[1]):                
#                 count+=1
#             if count == 4:
#                 # print(matrix[x][y])
#                 total += (1+ matrix[x][y])
# print(total)


# # for y,line in enumerate(matrix):
# #     for x,value in enumerate(line):
# #         if value < matrix[x+1][y]: 
# #             print(value)
# #         if value < matrix[x][y+1]:
# #             print(value)
# #         if value < matrix[x-1][y]: 
# #             print(value)
# #         if value < matrix[x][y-1]:
# #             print(value)
        


