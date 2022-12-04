from pytimedinput import timedInput
import os
import item
from colorama import Fore, init

WIDTH = 22
HEIGHT = 13
center_w = WIDTH//2
center_h = HEIGHT//2
item_and_pos = item.items(HEIGHT, WIDTH)
item_pos = item_and_pos[0]
item_eat = item_and_pos[1]
snake_body = [(center_h, center_w)]
part_snake = (center_h, center_w + 1)
DIRECTIONS = {'left': (0, -1), 'right': (0, 1), 'up': (-1, 0), 'down': (1, 0)}
direction = DIRECTIONS['right']
points = 0
init(autoreset=True)
CELLS = [(h, w) for h in range(HEIGHT) for w in range(WIDTH)]

def field():
    for c in CELLS:
        if c in snake_body:
            print(Fore.LIGHTGREEN_EX + '::', end='')
        elif c[1] in (0, WIDTH - 1) or c[0] in (0, HEIGHT - 1):
            print(Fore.LIGHTBLACK_EX + '##', end='')
        elif c == item_pos:
            print(item_eat, end='')
        else:
            print('  ', end='')
        if c[1] == WIDTH-1:
            print('')

def update_snake():
    if snake_body[0] == (snake_body[0][0], (WIDTH - 1)):
        new_head = (snake_body[0][0], 0) + DIRECTIONS['right']
        snake_body.insert(0, new_head)
        snake_body.pop(-1)
    elif snake_body[0] == (snake_body[0][0], 0):
        new_head = (snake_body[0][0], (WIDTH - 1)) + DIRECTIONS['left']
        snake_body.insert(0, new_head)
        snake_body.pop(-1)
    elif snake_body[0] == (0, snake_body[0][1]):
        new_head = ((HEIGHT - 1), snake_body[0][1]) + DIRECTIONS['up']
        snake_body.insert(0, new_head)
        snake_body.pop(-1)
    elif snake_body[0] == ((HEIGHT - 1), snake_body[0][1]):
        new_head = (0, snake_body[0][1]) + DIRECTIONS['down']
        snake_body.insert(0, new_head)
        snake_body.pop(-1)
    else:
        new_head = snake_body[0][0] + direction[0], snake_body[0][1] + direction[1]
        snake_body.insert(0, new_head)
        snake_body.pop(-1)

while True:
    os.system('cls')
    # print(f"SNAKE BODY:{snake_body}")
    print(Fore.LIGHTWHITE_EX + f"Points: {points}")
    field()
    if snake_body[0] == item_pos:
        points = points+1
        item_and_pos = item.items(HEIGHT, WIDTH)
        item_pos = item_and_pos[0]
        item_eat = item_and_pos[1]
        snake_body.append(part_snake)  # dodanie na koniec listy

    elif snake_body[0] in snake_body[1:]:
        print(Fore.RED + "GAME OVER")
        break
    txt,_ = timedInput('get input:', timeout = 0.2)
    match txt:
        case 'w': direction = DIRECTIONS['up']
        case 's': direction = DIRECTIONS['down']
        case 'a': direction = DIRECTIONS['left']
        case 'd': direction = DIRECTIONS['right']
        case 'z': break
    update_snake()
