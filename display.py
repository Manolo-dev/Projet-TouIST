import pygame
import re

with open('output.txt') as f:
    data = f.read()

data = re.findall(r"1 p\((\d),(\d),(\d),(\w+)\)", data)
print(data)
# data format is [(state, x, y, color), ...]

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Display")

clock = pygame.time.Clock()

for i in range(len(data)):
    if data[i][3] == "bleu":
        data[i] = (int(data[i][0]), int(data[i][1]), int(data[i][2]), (0, 0, 255))
    elif data[i][3] == "rouge":
        data[i] = (int(data[i][0]), int(data[i][1]), int(data[i][2]), (255, 0, 0))
    elif data[i][3] == "vert":
        data[i] = (int(data[i][0]), int(data[i][1]), int(data[i][2]), (0, 255, 0))
    elif data[i][3] == "orange":
        data[i] = (int(data[i][0]), int(data[i][1]), int(data[i][2]), (255, 165, 0))
    elif data[i][3] == "rose":
        data[i] = (int(data[i][0]), int(data[i][1]), int(data[i][2]), (255, 192, 203))
    elif data[i][3] == "vide":
        data[i] = (int(data[i][0]), int(data[i][1]), int(data[i][2]), (0, 0, 0))

square_size = 20
space_between_squares = 10

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    for x in data:
        pygame.draw.rect(screen, x[3], 
        (
            x[1]*(square_size+space_between_squares)+x[0]*100, 
            x[2]*square_size, 
            square_size, 
            square_size
        ))
        pygame.draw.rect(screen, (255, 255, 255),
        (
            x[1]*(square_size+space_between_squares)+x[0]*100,
            x[2]*square_size,
            square_size,
            square_size
        ), 1)

    pygame.display.flip()
