from point import Point
from parameters import WIN_SIZE
import random


def random_point():
    # Generate random point
    return Point(random.randint(0, WIN_SIZE), random.randint(0, WIN_SIZE))


def cluster4_point():
    # Generate random points but builds 4 clusters
    x = random.randint(0, WIN_SIZE)
    y = random.randint(0, WIN_SIZE)
    if x < WIN_SIZE / 4 or (x > WIN_SIZE / 2 and x < WIN_SIZE * 3 / 4):
        x += random.randint(0, WIN_SIZE / 4)
    else:
        x -= random.randint(0, WIN_SIZE / 4)

    if y < WIN_SIZE / 4 or (y > WIN_SIZE / 2 and y < WIN_SIZE * 3 / 4):
        y += random.randint(0, WIN_SIZE / 4)
    else:
        y -= random.randint(0, WIN_SIZE / 4)
    return Point(x, y)
