class PractiseNim:
    def __init__(self,piles = [15,9,12]):
        self.turn = 1
        self.piles = piles

    def is_game_over(self):
        return sum(self.piles) == 1

    def get_next_turn(self):
        return self.turn - 3

    def execute_move(self,move):
        pile = move[0]
        stones = int(move[1])
        self.piles[pile - 1] = self.piles[pile-1] - stones
        self.turn = self.get_next_turn()

    def get_pile(self):
        return self.piles

    def get_turn(self):
        return self.turn








