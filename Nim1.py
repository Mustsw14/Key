class Nim2:
    def __init__(self,piles=[15, 7, 9]):
        self._piles = piles
        self._turn = 1


    def is_game_over(self):
        return sum(self.piles) == 1


    def get_next_turn(self):
        return 3 - self.turn


    def execute_move(self,move):
        pile = move[0]
        stones_to_remove = move[1]
        self.piles[pile-1] -= stones_to_remove
        self_turn = self.get_next_turn()

    def get_piles(self):
        return self.piles

    def get_turn(self):
        return self.turn


