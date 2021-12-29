from collections import deque
matrix=[]
with open("day10_short.txt", "r") as f:
    lines = f.readline()
    while lines:
        line=(lines.strip("\n"))
        matrixline=[x for x in line]
        matrix.append(matrixline)        
        lines = f.readline()

# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.
closing_brackets=["}",")","]",">"]
opening_brackets=["{","(","[","<"]

bracketpair={
    "}":"{",
    "]":"[",
    ">":"<",
    ")":"(" }

errbrackets=[]
for line in matrix:
    stack = []
    # print(line)
    for bracket in line:
        if bracket in opening_brackets:
            stack.append(bracket)
        if bracket in closing_brackets:
            if bracketpair.get(bracket,"err")!=stack.pop():
                # print(bracket)
                errbrackets.append(bracket)
                break
# print(errbrackets)

costs={
    ")": 3,
    "]":57,
    "}":1197,
    ">":25137
}

cost=0
for errbracket in errbrackets:
    cost+=costs[errbracket]
    # print(costs[errbracket])
print(cost)

