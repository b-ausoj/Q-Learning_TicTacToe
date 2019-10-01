import random


class RandomPlayerTicTacToe:

    def __init__(self, name):

        self.name = name

        pass

    @staticmethod
    def make_move(board, episode, training):

        while True:
            random_number = random.randint(0, 8)
            if board[2][random_number] == 0.99:
                return random_number

    @staticmethod
    def buffer_experience(a, b, c, d, e):

        pass

    @staticmethod
    def evolve():

        pass

    @staticmethod
    def learn(a, b, c, d):

        pass
