from random import randint
import snakes_Pos


ladders = {}


# This function will generate ladders position randomly
def gen_ladders():
    number_of_ladders = int(input("Enter Ladders Count: "))
    i = 0
    while i < number_of_ladders:
        ladder_top = randint(11, 99)
        if ladder_top not in ladders:
            if ladder_top not in ladders.values():
                if ladder_top not in snakes_Pos.snakes:
                    if ladder_top not in snakes_Pos.snakes.values():
                        ladders[randint(2, ladder_top-6)] = ladder_top
                    i += 1
    print(ladders)
