import re

with open('output.txt') as f:
    data = f.read()

data = re.findall(r"1 p\((\d),(\d),(\d),(\w+)\)", data)
colors = {
    'vert': '\033[48;5;41m',
    'orange': '\033[48;5;214m',
    'bleu': '\033[48;5;75m',
    'rouge': '\033[48;5;197m',
    'rose': '\033[48;5;201m',
    'vide': '\033[48;5;234m',
}

for i in range(len(data)):
    data[i] = (int(data[i][0]), int(data[i][1]), int(data[i][2]), data[i][3])

size = [0, 0, 0]
for i in range(len(data)):
    if data[i][0] > size[0]:
        size[0] = data[i][0]
    if data[i][1] > size[1]:
        size[1] = data[i][1]
    if data[i][2] > size[2]:
        size[2] = data[i][2]
size = [size[0]+1, size[1], size[2]]
result = [[['vide']*size[2] for i in range(size[1])] for k in range(size[0])]

for e in data:
    result[e[0]][e[1]-1][e[2]-1] = e[3]

for i in range(size[0]):
    s = result[i]
    print("\n=== ÉTAPE", i, "===\n")
    for k in range(size[2]-1, -1, -1):
        for j in range(size[1]):
            t = s[j]
            e = t[k]
            print(colors[e] + "  " + '\033[0m', '', end="")
        print()