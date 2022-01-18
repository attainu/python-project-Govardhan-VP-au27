from n_Players import CountPlayer
from p_Names import PlayerNames
from w_Players import Welcome
import random
import snakes_Pos
import ladders_Pos
from p_Game import PlayGame


# This function is responsible for executing all the features of the game
def run():
    # randomly generated snakes positions
    snakes_Pos.gen_snakes()

    # randomly generated ladders positions
    ladders_Pos.gen_ladders()
    

    # number of players playing the game
    num_of_players = CountPlayer.players_count()

    # Getting the player names
    global players_names
    players_names = PlayerNames.name_of_players(num_of_players)

    # Welcome the players to the game
    Welcome.welcome_players(players_names)

    # This code will execute in case there is only one player
    if num_of_players < 2:
        PlayGame.play_single_player_game(num_of_players, players_names)

    # This code will execute when players are more than one
    else:
        PlayGame.play_multi_player_game(num_of_players, players_names)


if __name__ == '__main__':
    run()
