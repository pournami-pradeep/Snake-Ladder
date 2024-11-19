import random


class SnakeandLadder:

    def __init__(self, player) -> None:
        self.curr_pos = 0
        self.player = player
        self.name = None
        self.snake_ladder = {6: 30, 24: 50, 55: 79, 85: 98, 99: 25, 40: 15, 19: 3}
        self.next_player = None
        self.color = None
        

    def update_pos(self, val):
        if self.curr_pos == 0 and val != 1:
            self.curr_pos = 0
            return 0
        pos = self.curr_pos + val
        
        if self.snake_ladder.get(pos):
            self.curr_pos = self.snake_ladder[pos]
        else:
            self.curr_pos = pos
        return self.curr_pos
    
    def update_player(self,player):
        self.next_player = player
        return self.next_player