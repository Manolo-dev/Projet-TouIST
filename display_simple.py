import re

with open('output.txt') as f:
    datas = f.read()

tubes = re.findall(r"1 p\((\d+),(\d+),(\d+),(\w+)\)", datas)

colors = {
    'vert': '\033[48;5;41m',
    'orange': '\033[48;5;214m',
    'bleu': '\033[48;5;75m',
    'rouge': '\033[48;5;197m',
    'rose': '\033[48;5;201m',
    'vide': '\033[48;5;234m',
}

#===============#
#===| TUBES |===#
#===============#

# parse to int
for i in range(len(tubes)):
    tubes[i] = (int(tubes[i][0]), int(tubes[i][1]), int(tubes[i][2]), tubes[i][3])

# define size of 3D matrice
size_tubes = [0, 0, 0]
for i in range(len(tubes)):
    if tubes[i][0] > size_tubes[0]:
        size_tubes[0] = tubes[i][0]
    if tubes[i][1] > size_tubes[1]:
        size_tubes[1] = tubes[i][1]
    if tubes[i][2] > size_tubes[2]:
        size_tubes[2] = tubes[i][2]

size_tubes = [size_tubes[0]+1, size_tubes[1], size_tubes[2]]

# create 3D matrice
result_tubes = [[['vide']*size_tubes[2] for i in range(size_tubes[1])] for k in range(size_tubes[0])]

# allocate each value in list of tubes in 3D matrice
for e in tubes:
    result_tubes[e[0]][e[1]-1][e[2]-1] = e[3]

tubes = result_tubes

#==============#
#===| SHOW |===#
#==============#

for i in range(size_tubes[0]):
    s = tubes[i]
    print("\n=== ÉTAPE", i, "===\n")
    for k in range(size_tubes[2]-1, -1, -1):
        for j in range(size_tubes[1]):
            char = "   "
            t = s[j]
            e = t[k]
            print(colors[e] + char + '\033[0m', '', end="")
        print()