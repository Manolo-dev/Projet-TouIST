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

j = [0, 0, 0]
for i in range(len(data)):
    if data[i][0] > j[0]:
        j[0] = data[i][0]
    if data[i][1] > j[1]:
        j[1] = data[i][1]
    if data[i][2] > j[2]:
        j[2] = data[i][2]
j = [j[0]+1, j[1], j[2]]
result = [[['vide']*j[1] for i in range(j[2])] for k in range(j[0])]

for e in data:
    result[e[0]][e[2]-1][e[1]-1] = e[3]

for i in range(len(result)):
    s = result[i]
    print("\n=== ÉTAPE", i, "===\n")
    for t in s:
        for e in t:
            print(colors[e] + "  " + '\033[0m', '', end="")
        print()t.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for x in data:
        pygame.draw.rect(screen, x[3], 
        (
            x[1]*(square_size+space_between_squares)+x[0]*100, 
            (4-x[2])*square_size, 
            square_size, 
            square_size
        ))
        pygame.draw.rect(screen, (255, 255, 255),
        (
            x[1]*(square_size+space_between_squares)+x[0]*100,
            (4-x[2])*square_size,
            square_size,
            square_size
        ), 1)

    pygame.display.flip()
