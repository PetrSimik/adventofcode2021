# Dijkstra's shortest path algorithm
from heapq import heappop,heappush

def get_neigh(r,c):
    return[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]

with open("d15.txt","r") as file:
    lines = file.readlines()
    
matrix = [[int(item) for item in line.strip()] for line in lines]

print(len(matrix)-1,len(matrix[0])-1)
R=len(matrix)
C=len(matrix[0])
queue = [(0,(0,0))]
locked=set()

while queue:
    risk,pos = heappop(queue)
    if pos == (R-1, C-1):
        break
    if pos in locked:
        continue
    locked.add(pos)

    for r,c in get_neigh(*pos):
        if 0 <= r < R and 0 <= c < C:
            value=risk + matrix[r][c]
            heappush(queue, (value, (r,c)))

print("part1",risk)
     