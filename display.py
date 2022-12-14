import re
from getch import getch

with open('output.txt') as f:
    datas = f.read()

tubes = re.findall(r"1 p\((\d+),(\d+),(\d+),(\w+)\)", datas)

colors_b = {
    'vert':   '\033[48;2;087;255;087m',
    'orange': '\033[48;2;255;171;087m',
    'bleu':   '\033[48;2;087;087;255m',
    'rouge':  '\033[48;2;255;087;087m',
    'rose':   '\033[48;2;255;087;255m',
    'vide':   '\033[48;2;026;026;026m',
}

colors_f = {
    'vert':   '\033[38;2;087;255;087m',
    'orange': '\033[38;2;255;171;087m',
    'bleu':   '\033[38;2;087;087;255m',
    'rouge':  '\033[38;2;255;087;087m',
    'rose':   '\033[38;2;255;087;255m',
    'vide':   '\033[38;2;026;026;026m',
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
    space = ' ' if len(str(i)) % 2 == 0 else ''
    sl    = 1 if len(str(i)) % 2 == 0 else 0
    print()
    print("\033[1;31m", end="")
    print(" " * ((6*size_tubes[1] - len(str(i)) - 13 - sl)//2) + "╔"  + ""           +  "═"*(10  + sl    + len(str(i))) + ""           +  "╗")
    print(" " * ((6*size_tubes[1] - len(str(i)) - 13 - sl)//2) + "║┏" + ""           +  "━"*(8   + sl    + len(str(i))) + ""           + "┓║")
    print(" " * ((6*size_tubes[1] - len(str(i)) - 13 - sl)//2) + "║┃" + "\033[1;34m" + " ÉTAPE " + space + str(i) + " " + "\033[1;31m" + "┃║")
    print(" " * ((6*size_tubes[1] - len(str(i)) - 13 - sl)//2) + "║┗" + ""           +  "━"*(8   + sl    + len(str(i))) + ""           + "┛║")
    print(" " * ((6*size_tubes[1] - len(str(i)) - 13 - sl)//2) + "╚"  + ""           +  "═"*(10  + sl    + len(str(i))) + ""           +  "╝")
    print("\033[0m")
    for j in range(size_tubes[1]):
        print("\033[1;31m🭾"+colors_b['vide']+"   "+"\033[0m\033[1;31m🭽\033[0m ", end="")
    print()
    for k in range(size_tubes[2]-1, -1, -1):
        for _ in range(3):
            print("\033[1;31m▕\033[1;0m", end="")
            for j in range(size_tubes[1]):
                t = s[j]
                e = t[k]
                char = "   "
                if _ == 0 and ((k+1 < size_tubes[2] and t[k+1] == 'vide') or (k+1 == size_tubes[2])) and e != 'vide':
                    char = colors_f['vide']+"▝▀▘" # ▜█▛    ▛ ▜    ▛▜▛    ▓▓▓
                if _ == 2 and k != 0 and e != "vide":
                    char = "▁▁▁"
                print(colors_b[e] + char + '\033[0m' + ('\033[1;31m▏\033[1;0m ' if j < size_tubes[1] else '') + ('\033[1;31m▕\033[1;0m' if j < size_tubes[1]-1 else ''), end="")
            print()
    print(" ", end="")
    for j in range(size_tubes[1]):
        print("\033[1;31m▔▔▔\033[1;0m   ", end="")
print()

getch()