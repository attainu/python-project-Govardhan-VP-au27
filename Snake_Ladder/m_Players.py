

import random
import snakes_Pos
import ladders_Pos


class MovePlayer:

    def move(player, value):
        roll_dice = random.randint(1, 6)
        num = value + roll_dice
        if num > 100:
            print(f"BAD LUCK, YOU CANT MOVE, YOU NEED {100 - value} TO WIN\n")
            return value

        if num == 100:
            return num

        # IF PLAYER IS NOT REACHED HOME
        print(
            player, "Rolled a : ", roll_dice, " and moved from :", value, " to :",
            num, '\n')

        # TO CHECK IF PLAYER STOPPED ON SNAKE HEAD
        if num in snakes_Pos.snakes:
            print(
                player, " got bitten by a snake and is now on",
                snakes_Pos.snakes[num], '\n'
                )
            num = snakes_Pos.snakes[num]
           

        # IF PLAYER IS ON LADDER BOTTOM IT WILL CLIMB THE LADDER
        if num in ladders_Pos.ladders:
            print(
                player, "Climbed the ladder and is now on ",
                ladders_Pos.ladders[num], '\n'
                )
            num = ladders_Pos.ladders[num]
           
        return num
