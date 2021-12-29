data =[]
with open("day8_short.txt") as file:
    line = file.readline()
    while line:
        left = sorted(["".join(sorted(x) for x in  line.strip("\n").split("|"))[0].split()], key = len)
        
        print(left)


