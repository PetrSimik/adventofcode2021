data ={}
with open("2021_d6_full.txt") as f:
    fishes = [int(x) for x in  f.readline().split(',')]
    for value in range(9):
         data[value] = 0
    for element in fishes:
        data[element] +=1

for days in range(256):
    zeros = data[0]
    data[0] = 0
    for index in range(1,len(data)):
        data[index-1] += data[index]
        data[index] = 0
    data[6] += zeros
    data[8] += zeros
print(data)
result=0
for key,value in data.items():
    result += value

print(f"vysledek je {result}")

