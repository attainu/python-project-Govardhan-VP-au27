
from random import randint


snakes = {}

# This function will generate ladders position randomly
def gen_snakes():
    number_of_snakes = int(input("Enter snakes Count: "))

    i = 0
    while i < number_of_snakes:
        snake_head = randint(11, 99)
        if snake_head not in snakes:
            if snake_head not in snakes.values():
                snakes[snake_head] = randint(2, snake_head-6)

            i += 1
    print(snakes)

