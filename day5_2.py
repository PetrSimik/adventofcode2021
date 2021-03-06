lines=[]
with open("input5.txt") as f:        
    line=f.readline()
    while line:
        line=line.strip('\n').split(' ')
        left = [int(x) for x in line[0].split(',')]
        right = [int(x) for x in line[2].split(',')]
        lines.append([left,right])
        line = f.readline()
print(lines)
               

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
    else:
        if line[0][0] > line[1][0]:
            line = [line[1],line[0]]
        for spot in range(line[1][0]- line[0][0]+1):
            vertical = spot if line[1][1] > line[0][1] else -spot
            horizontal = spot if line[1][0] > line[0][0] else -spot
            grid[line[0][0] + horizontal][line[0][1] + vertical] +=1

count=0
for row in grid:
    for element in row:
        if element >= 2:
            count +=1
print(f"solution p2 {count}")