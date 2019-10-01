class HumanPlayerTicTacToe:

    def __init__(self, name, game_stone):

        self.name = name

        self.board = None

        self.cross = "O"
        self.naught = "X"
        self.my_stone = game_stone

        if game_stone == self.cross:
            self.rival_stone = self.naught
        else:
            self.rival_stone = self.cross

        # das mit den steinen noch nicht sehr elegant gelöst

        pass

    @staticmethod
    def draw_board(board):

        print('\n ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
        print('-----------')
        print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
        print('-----------')
        print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

    def prepare_board(self, board):

        self.board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

        for i in range(len(board[0])):
            if board[0][i] == 0.99:
                self.board[i] = self.my_stone
            elif board[1][i] == 0.99:
                self.board[i] = self.rival_stone

    def make_move(self, board, episode, training):

        self.prepare_board(board)
        self.draw_board(self.board)

        while True:
            players_choice = int(input("\nYour turn {} : ".format(self.name)))
            if board[2][players_choice] == 0.99:
                return players_choice

    @staticmethod
    def buffer_experience(a, b, c, d, e):

        pass

    @staticmethod
    def evolve():

        pass