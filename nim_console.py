from NNim import Nim


def read_move(game):
   move = input(f"Player turn {game.get_turn()}, enter your move (pile,stones):")
   pile = int(move[0])
   stones_to_remove = int(move[2])
   return pile,stones_to_remove


def display_game(games):
    print(f"Piles: {games.get_piles()}")


def main():
    game = Nim()


    while not game.is_game_over():
        display_game(game)
        move = read_move(game)
        game.execute_move(move)


    print(f"\n\nFinal Piles: {game.get_piles()}")
    print(f"Player {game.get_next_turn()} is the winner")
    print("Thanks for playing")


if __name__ == '__main__':
    main()