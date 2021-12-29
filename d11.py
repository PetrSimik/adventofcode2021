from collections import defaultdict
import sys
sys.setrecursionlimit(5000)

matrix=[]
count = 0
with open("day11_short.txt", "r") as f:
    lines = f.readline()
    while lines:
        line=(lines.strip("\n"))
        matrixline=[x for x in line]
        matrix.append(matrixline)        
        lines = f.readline()
field=defaultdict(int)
for x,value in enumerate(matrix):
    for y,value in enumerate(value):        
        field[(x,y)] =int(matrix[x][y])

arounds = [[x+1,y],[x-1,y],[x,y+1],[x,y-1],[x+1,y+1],[x+1,y-1],[x-1,y+1],[x-1,y-1]]

def blast(x,y):
    global count
    for key in arounds:
        (a,b) = key          
        if (a,b) in field:
            if field[(a,b)]==9:
                count +=1
                field[(a,b)]=0
                blast(a,b)            
            field[(a,b)]+=1
    
#steps

for repeat in range(100):
    for x in range(10):
        for y in range(10):        
            if field[x,y] == 9:
                blast(x,y)
                count+=1
                field[x,y] = 0
            field[x,y]+=1

print(field)
print(count)


    

    
