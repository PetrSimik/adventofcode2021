
matrix=[]
with open("day10.txt", "r") as f:
    lines = f.readline()
    while lines:
        line=(lines.strip("\n"))
        matrixline=[x for x in line]
        matrix.append(matrixline)        
        lines = f.readline()

closing_brackets=["}",")","]",">"]
opening_brackets=["{","(","[","<"]

costs={
    ")": 3,
    "]":57,
    "}":1197,
    ">":25137
}

bracketpair={
    "}":"{",
    "]":"[",
    ">":"<",
    ")":"(" }

incomplete =[]
errbrackets=[]
for line in matrix:
    stack = []
    # print(line)
    corrupted=False
    for bracket in line:
        if bracket in opening_brackets:
            stack.append(bracket)            
        elif bracket in closing_brackets:
            if bracketpair.get(bracket,"err")!=stack.pop():                
                errbrackets.append(bracket)                
                corrupted=True                
                break
    if corrupted==False:
        incomplete.append(stack)        

costs={
    "(":1,
    "[":2,
    "{":3,
    "<":4
}

points =[]
for line in incomplete:
    total=0
    for bracket in reversed(line):
        total *=5
        total += costs[bracket]
    print(total)
    print(line)
    points.append(total)

print("p2",sorted(points)[len(points)//2])




    

# print(errbrackets)




# cost=0
# for errbracket in errbrackets:
#     cost+=costs[errbracket]
#     # print(costs[errbracket])
# print(cost)

