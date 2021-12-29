lines=[]
with open("input5.txt") as f:        
    line=f.readline()
    while line:
        line=line.strip('\n').split(' ')
        left = [int(x) for x in line[0].split(',')]
        right = [int(x) for x in line[2].split(',')]
        lines.append([left,right])
        line = f.readline()
        

print(lines[0])

grid = [[0]* 1000 for i in range(1000)]
for line in lines:
    # print(line)
    if line[0][0]==line[1][0]:
        a=min(line[0][1], line[1][1])
        b=max(line[0][1], line[1][1])   
        for index in range(a,b+1):
            grid[line[0][0]][index] += 1
    elif line[0][1]==line[1][1]:
        a=min(line[0][0], line[1][0])
        b=max(line[0][0], line[1][0])
        # print(a,b)
        for index in range(a,b+1):
            grid[index][line[0][1]] += 1
count=0
for row in grid:
    for element in row:
        if element >= 2:
            count +=1
print(f"solution p1 {count}")