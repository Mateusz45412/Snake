import random
def items(HEIGHT, WIDTH):
    eat = ['😺', '🐭', '🐯', '🦁', '🐮', '🐷', '🐸', '🐤', '🐦', '🐔', '🦆', '🦅', '🐛', '🐴', '🐛',
           '🐢', '🦕', '🦞', '🐅', '🐋']

    pos_W = random.randint(1, WIDTH-2)
    pos_H = random.randint(1, HEIGHT-2)
    item_pos = (pos_H, pos_W)
    computer_item = random.choice(eat)

    return item_pos, computer_item
