from board import Board
from agent import Agent
class Gomoku:
    def _init_(self):
        self.agent1 = Agent(1)
        self.agent2 = Agent(2)
        self.board = Board()

    def play(self):
        while True:
            if self.agent1.strategy1(self.board):
            elif self.agent1.strategy2(self.board):
            elif self.agent1.strategy3(self.board):
            elif self.agent1.strategy4(self.board):

            if self.agent2.strategy1(self.board):
            elif self.agent2.strategy2(self.board):
            elif self.agent2.strategy3(self.board):
            elif self.agent2.strategy4(self.board):
                
            if self.agent1.win(self.board):
                print("Agent 1 wins!")
                return
            if self.agent2.win(self.board):
                print("Agent 2 wins!")
                return


game = Gomoku()
game.play()
